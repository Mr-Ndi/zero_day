from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class BookCreate(BaseModel):
    title: str = Field(..., examples = "Uwahanuriwe")
    author: str = Field(..., examples = "John Doe")
    publisher: str = Field(..., examples = "ABC Publishing")
    publication_date: date = Field(..., examples = "2023-01-01")
    pages: int = Field(..., examples = 300)
    language: str = Field(..., examples = "English")
    isbn: str = Field(..., examples = "978-3-16-148410-0")
    summary: str = Field(..., examples = "A brief summary of the book.")

class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True

class BookUpdate(BaseModel):
    title: Optional[str] = Field(..., examples = "Uwahanuriwe2")
    author: Optional[str] = Field(..., examples = "John Doe2")
    publisher: Optional[str] = Field(..., examples = "ABC Publishing2")
    publication_date: Optional[date] = Field(..., examples = "2023-01-02")
    pages: Optional[int] = Field(..., examples = 302)
    language: Optional[str] = Field(..., examples = "English2")
    isbn: Optional[str] = Field(..., examples = "978-3-16-148410-02")
    summary: Optional[str] = Field(..., examples = "A brief summary of the book 2.")
