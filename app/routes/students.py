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
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid authorization header")
    token = authorization.split(" ")[1]
    try:
        payload = jwt.decode(token, settings.JWT_SECRET, algorithms=[settings.JWT_ALGORITHM])
        user_id = int(payload.get("sub"))
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/me", response_model=StudentOut)
def get_my_profile(current_user: User = Depends(get_current_user)):
    """Return the currently logged-in student's profile"""
    if not current_user.student:
        raise HTTPException(status_code=401, detail="User is not a student")
    return current_user.student
