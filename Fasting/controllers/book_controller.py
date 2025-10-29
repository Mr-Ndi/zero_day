from handler import engine
from fastapi import HTTPException
from models.book_model import Book
from middleware.schemas import BookCreate, BookUpdate
from service.book_service import insert_book, get_book_by_id, get_all_books, delete_book, update_book

async def get_book(book_id: int):
    book = await get_book_by_id(engine, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
    
async def get_books():
    books = await get_all_books(engine)
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books

async def create_book(book: BookCreate):
    new_book = await insert_book(engine, book=book)
    if not new_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return new_book

async def remove_book(book_id: int):
    result = delete_book(book_id=book_id)
    return result

async def modify_book(book_id: int, updated_book: BookUpdate):
    if not book_id:
        raise HTTPException(status_code=404, detail="Book not found")
    book = await get_book_by_id(engine, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book = await update_book(engine, old_book=book, updated_book=updated_book)
    return book

