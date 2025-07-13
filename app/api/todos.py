from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, db, auth

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.post('/', response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(db.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.create_todo(db, todo, current_user.id) # type: ignore

@router.get('/', response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(db.get_db), current_user: models.User = Depends(auth.get_current_user)):
    return crud.get_todos(db, current_user.id) # type: ignore

@router.get('/{todo_id}', response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(db.get_db), current_user: models.User = Depends(auth.get_current_user)):
    todo = crud.get_todo_by_id(db, todo_id, current_user.id) # type: ignore
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@router.put('/{todo_id}', response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(db.get_db), current_user: models.User = Depends(auth.get_current_user)):
    todo = crud.update_todo(db, todo_id, current_user.id, todo_update) # type: ignore
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@router.delete('/{todo_id}', response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(db.get_db), current_user: models.User = Depends(auth.get_current_user)):
    todo = crud.delete_todo(db, todo_id, current_user.id) # type: ignore
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo
    
