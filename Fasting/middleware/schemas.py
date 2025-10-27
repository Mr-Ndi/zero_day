from pydantic import BaseModel
from typing import Optional
from datetime import date

class BookCreate(BaseModel):
    title: str
    author: str
    publisher: str
    publication_date: date
    pages: int
    language: str
    isbn: str
    summary: str

class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    publisher: Optional[str] = None
    publication_date: Optional[date] = None
    pages: Optional[int] = None
    language: Optional[str] = None
    isbn: Optional[str] = None
    summary: Optional[str] = None
