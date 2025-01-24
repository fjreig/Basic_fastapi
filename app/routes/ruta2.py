from fastapi import APIRouter, Body, Depends, Path, Query

from app.auth.auth_handler import signJWT, decodeJWT
from app.auth.auth_bearer import JWTBearer

router = APIRouter()

@router.get("/whoiam", summary="Who I am", dependencies=[Depends(JWTBearer())])
async def create_user(token=Depends(JWTBearer())):
    variable = decodeJWT(token)
    return(variable)