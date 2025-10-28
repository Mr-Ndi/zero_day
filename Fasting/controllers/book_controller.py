from fastapi import HTTPException
from models.book_model import Book
from middleware.schemas import BookCreate, BookUpdate
from service.book_service import insert_book, get_book_by_id, get_all_books, delete_book, update_book

def get_book(book_id: int):
    book = get_book_by_id(book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
    
def get_books():
    books = get_all_books()
    if not books:
        raise HTTPException(status_code=404, detail="Books not found")
    return books

def create_book(book: BookCreate):
    new_book = insert_book(book=book)
    if not new_book:
        raise HTTPException(status_code=404, detail="Book not found")
    return new_book

def remove_book(book_id: int):
    result = delete_book(book_id=book_id)
    return result

def modify_book(book_id: int, updated_book: BookUpdate):
    if not book_id:
        raise HTTPException(status_code=404, detail="Book not found")
    book = get_book_by_id(book_id=book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    book = update_book(old_book=book, updated_book=updated_book)
    return book

