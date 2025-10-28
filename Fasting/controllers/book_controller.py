from sqlmodel import Session, en
from models.book_model import Book
from service.book_service import insert_book, get_book_by_id, get_all_books, delete_book, update_book

def get_book(book_id: int):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        return book
    
def get_books():
    with Session(engine) as session:
        pass