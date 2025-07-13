from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

# User CRUD operations
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate, hashed_password: str):
    db_user = models.User(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Todo CRUD operations
def create_todo(db: Session, todo: schemas.TodoCreate, user_id: int):
    db_todo = models.Todo(
        title=todo.title,
        description=todo.description,
        completed=todo.completed,
        owner_id=user_id,
        created_at=datetime.now(),
        due_date=todo.due_date,
        priority=todo.priority,
        category=todo.category
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def get_todos(db: Session, user_id: int):
    return db.query(models.Todo).filter(models.Todo.owner_id == user_id).all()

def get_todo_by_id(db: Session, todo_id: int, user_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id == user_id).first()

def update_todo(db: Session, todo_id: int, user_id: int, todo_update: schemas.TodoUpdate):
    db_todo = get_todo_by_id(db, todo_id, user_id)
    if not db_todo:
        return None
    for field, value in todo_update.model_dump().items():
        setattr(db_todo, field, value)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int, user_id: int):
    db_todo = get_todo_by_id(db, todo_id, user_id)
    if not db_todo:
        return None
    db.delete(db_todo)
    db.commit()
    return db_todo
