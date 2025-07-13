from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = 'sqlite:///./todo.db'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()

def create_tables():
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")
