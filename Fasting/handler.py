from sqlmodel import Session, SQLModel, create_engine
from models.book_model import Book
from contextlib import asynccontextmanager

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)