# Define the shape of data for requests and responses (validation and serialization)

from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import datetime

class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False
    due_date: Optional[datetime] = None
    priority: Optional[int] = 1
    category: Optional[str] = None

class TodoCreate(TodoBase):
    pass

class TodoUpdate(TodoBase):
    pass

class TodoResponse(TodoBase):
    id: int
    owner_id: int
    created_at: datetime

    class Config:
        orm_mode = True # Make Pydantic model compatible with ORM objects (orm objects can be converted to dict)

class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    todos: List[TodoResponse] = []

    class Config:
        orm_mode = True
