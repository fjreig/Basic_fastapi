from fastapi import APIRouter, Body, Depends, Path, Query
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from app.auth.auth_handler import signJWT, decodeJWT
from app.auth.auth_bearer import JWTBearer
from app.models import UserLoginSchema, Usuarios, UserRequest

from app.database import SessionLocal

# Dependency for database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def check_user(data: UserLoginSchema):
    users = []
    for user in users:
        if user.email == data.email and user.password == data.password:
            return True
    return False

router = APIRouter()

@router.post("/user/signup", summary="Create User")
async def create_user(notification_req: UserRequest, db: Session = Depends(get_db)):
    try:
        notification = Usuarios(
            email=notification_req.email,
            fullname=notification_req.fullname,
            rol=notification_req.rol,
            password=notification_req.password,
        )
        db.add(notification)
        db.commit()
        db.refresh(notification)
        return ({
            "email": notification_req.email, 
            "fullname": notification_req.fullname,
            "rol": notification_req.rol
            })
    except:
        return {"error": "Fallo al crear nuevo usuario"}

@router.post("/user/login", summary="Login")
async def user_login(data: UserLoginSchema = Body(...), db: Session = Depends(get_db)):
    data = jsonable_encoder(data)
    notification = db.query(Usuarios).filter(Usuarios.email == data['email'], Usuarios.password == data['password']).first()
    if notification is None:
        return {"error": "Wrong login details!"}
    return signJWT(notification.email, notification.rol)