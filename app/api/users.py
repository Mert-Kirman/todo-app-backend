from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, db
from passlib.context import CryptContext

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/register', response_model=schemas.UserResponse)
def register_user(user: schemas.UserCreate, db: Session = Depends(db.get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    hashed_password = pwd_context.hash(user.password)
    return crud.create_user(db, user, hashed_password)
