from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Student, User
from app.schemas import StudentOut
from app.config import settings
import jwt

router = APIRouter()

def get_current_user(token: str, db: Session):
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload.get("sub"))
        return db.query(User).filter(User.id == user_id).first()
    except:
        return None

@router.get("/me", response_model=StudentOut)
def get_my_profile(token: str, db: Session = Depends(get_db)):
    user = get_current_user(token, db)
    if not user or not user.student:
        raise HTTPException(status_code=401, detail="Unauthorized or not a student")
    return user.student
