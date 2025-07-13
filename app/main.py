from fastapi import FastAPI
from app.db import create_tables
from app.api import todos, users
from fastapi.middleware.cors import CORSMiddleware

create_tables()

app = FastAPI()

# CORS middleware to allow cross-origin requests
allowed_origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods
    allow_headers=["*"],  # Allows all headers
)

app.include_router(users.router)
app.include_router(todos.router)

# Health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}