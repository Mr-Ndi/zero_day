from sqlmodel import Session, en
from models.book_model import Book
from service.book_service import insert_book, get_book_by_id, get_all_books, delete_book, update_book

def get_book(book_id: int):
    book = get_book_by_id(book_id=book_id)
    return book
    
def get_books():
    books = get_all_books()
    return books

def create_book(book: Book):
    new_book = insert_book(book=book)
    return new_book

def remove_book(book_id: int):
    result = delete_book(book_id=book_id)
    return result

def modify_book(book_id: int, updated_book: Book):
    book = update_book(book_id=book_id, updated_book=updated_book)
    return book

