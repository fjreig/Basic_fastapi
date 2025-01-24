from fastapi import APIRouter, Body, Depends, Path, Query, HTTPException
from sqlalchemy.orm import Session

from app.auth.auth_handler import signJWT, decodeJWT
from app.auth.auth_bearer import JWTBearer
from app.models import Ficheros, FicherosRequest

from app.database import SessionLocal

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

router = APIRouter()

@router.post("/new", summary="Nuevo Fichero", dependencies=[Depends(JWTBearer())])
async def add_post(ficheros_req: FicherosRequest, db: Session = Depends(get_db)):
    notification = Ficheros(
        title=ficheros_req.title,
        content=ficheros_req.content,
    )
    db.add(notification)
    db.commit()
    db.refresh(notification)
    return {'title': ficheros_req.title, 'content':ficheros_req.content}

@router.get("/consultar/{id_fichero}", summary="Login")
async def user_login(id_fichero: str, db: Session = Depends(get_db)):
    notification = db.query(Ficheros).filter(Ficheros.id == id_fichero).first()
    if notification is None:
        return HTTPException(
                status_code=204,
                detail="No Content",
                headers={"X-Error": "No Content"},
            )
    return ({
            "title": notification.title, 
            "content": notification.content,
            "created_at": notification.created_at
            })