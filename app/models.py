from pydantic import BaseModel, Field, EmailStr
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Usuarios(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, index=True)
    fullname = Column(String)
    rol = Column(String)
    password = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

# Pydantic model for request validation
class UserRequest(BaseModel):
    fullname: str
    rol: str
    email: EmailStr
    password: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "John Smith",
                "rol": "admin",
                "email": "smith@x.com",
                "password": "weakpassword"
            }
        }

class Ficheros(Base):
    __tablename__ = "ficheros"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    
class FicherosRequest(BaseModel):
    title: str = Field(...)
    content: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Securing FastAPI applications with JWT.",
                "content": "How secure your application by enabling authentication using JWT."
            }
        }

class UserSchema(BaseModel):
    fullname: str = Field(...)
    rol: str = Field(...)
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "fullname": "John Smith",
                "rol": "admin",
                "email": "smith@x.com",
                "password": "weakpassword"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr = Field(...)
    password: str = Field(...)

    class Config:
        json_schema_extra = {
            "example": {
                "email": "smith@x.com",
                "password": "weakpassword"
            }
        }