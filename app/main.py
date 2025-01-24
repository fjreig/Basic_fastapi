from fastapi import FastAPI, Body, Depends

from app.routes.ruta1 import router as Ruta1
from app.routes.ruta2 import router as Ruta2
from app.routes.ruta3 import router as Ruta3

from app.database import init_db

# Initialize the database
init_db()

app = FastAPI()

tags_metadata = [
    {
        "name": "Usuario",
        "description": "Login",
    },{
        "name": "Check",
        "description": "Check User",
    },{
        "name": "Upload",
        "description": "Upload docs",
    }
]

app.include_router(Ruta1, tags=["Usuario"], prefix="/Usuario")
app.include_router(Ruta2, tags=["Check"], prefix="/Check")
app.include_router(Ruta3, tags=["Upload"], prefix="/Upload")