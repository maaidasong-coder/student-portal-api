from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[str] = "student"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class StudentOut(BaseModel):
    id: int
    matric_no: str
    name: str
    program: str
    level: str
    session: str

    class Config:
        orm_mode = True
