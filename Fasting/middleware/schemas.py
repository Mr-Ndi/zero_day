from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class BookCreate(BaseModel):
    title: str = Field(None, examples = ["Uwahanuriwe"])
    author: str = Field(None, examples = ["John Doe"])
    publisher: str = Field(None, examples = ["ABC Publishing"])
    publication_date: date = Field(None, examples = ["2023-01-01"])
    pages: int = Field(None, examples = [300])
    language: str = Field(None, examples = ["English"])
    isbn: str = Field(None, examples = ["978-3-16-148410-0"])
    summary: str = Field(None, examples = ["A brief summary of the book."])

class BookRead(BookCreate):
    id: int

    class Config:
        orm_mode = True

class BookUpdate(BaseModel):
    title: Optional[str] = Field(None, examples = ["Uwahanuriwe2"])
    author: Optional[str] = Field(None, examples = ["John Doe2"])
    publisher: Optional[str] = Field(None, examples = ["ABC Publishing2"])
    publication_date: Optional[date] = Field(None, examples = ["2023-01-02"])
    pages: Optional[int] = Field(None, examples = [302])
    language: Optional[str] = Field(None, examples = ["English2"])
    isbn: Optional[str] = Field(None, examples = ["978-3-16-148410-02"])
    summary: Optional[str] = Field(None, examples = ["A brief summary of the book 2."])
