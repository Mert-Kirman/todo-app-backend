from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, crud, db

router = APIRouter(
    prefix="/todos",
    tags=["todos"]
)

@router.post('/', response_model=schemas.TodoResponse)
def create_todo(todo: schemas.TodoCreate, db: Session = Depends(db.get_db), user_id: int = 1):
    # TODO: Replace user_id with actual authenticated user ID
    return crud.create_todo(db, todo, user_id)

@router.get('/', response_model=list[schemas.TodoResponse])
def read_todos(db: Session = Depends(db.get_db), user_id: int = 1):
    return crud.get_todos(db, user_id)

@router.get('/{todo_id}', response_model=schemas.TodoResponse)
def read_todo(todo_id: int, db: Session = Depends(db.get_db), user_id: int = 1):
    todo = crud.get_todo_by_id(db, todo_id, user_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@router.put('/{todo_id}', response_model=schemas.TodoResponse)
def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, db: Session = Depends(db.get_db), user_id: int = 1):
    todo = crud.update_todo(db, todo_id, user_id, todo_update)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo

@router.delete('/{todo_id}', response_model=schemas.TodoResponse)
def delete_todo(todo_id: int, db: Session = Depends(db.get_db), user_id: int = 1):
    todo = crud.delete_todo(db, todo_id, user_id)
    if not todo:
        raise HTTPException(status_code=404, detail='Todo not found')
    return todo
    
