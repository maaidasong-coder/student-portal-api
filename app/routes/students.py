from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Student, User
from app.schemas import StudentOut
from app.config import settings
import jwt

router = APIRouter(
    prefix="/students",
    tags=["Students"]
)

def get_current_user(authorization: str = Header(...), db: Session = Depends(get_db)):
    """Decode JWT from Authorization header"""
    try:
        token = authorization.split(" ")[1]  # Bearer <token>
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload.get("sub"))
        return db.query(User).filter(User.id == user_id).first()
    except Exception:
        return None


@router.get("/me", response_model=StudentOut)
def get_my_profile(current_user: User = Depends(get_current_user)):
    """Return the currently logged-in student's profile"""
    if not current_user or not current_user.student:
        raise HTTPException(status_code=401, detail="Unauthorized or not a student")
    return current_user.student
