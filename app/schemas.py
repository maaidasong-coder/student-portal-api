from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


# ===============================
# USER SCHEMAS
# ===============================

class UserBase(BaseModel):
    email: EmailStr
    role: Optional[str] = "student"


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True


# ===============================
# TOKEN SCHEMAS
# ===============================

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


# ===============================
# STUDENT SCHEMAS
# ===============================

class StudentOut(BaseModel):
    id: int
    matric_no: str
    name: str
    program: Optional[str] = None
    level: Optional[str] = None
    session: Optional[str] = None

    class Config:
        orm_mode = True
