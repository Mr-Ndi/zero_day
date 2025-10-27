from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import date
from enum import Enum



class Book(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    author: str
    publisher: str
    publication_date: date
    pages: int
    language: str
    isbn: str
    summary: str