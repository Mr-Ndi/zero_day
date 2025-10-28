from sqlmodel import Session, select
from models.book_model import Book

def insert_book(engine, book):
    with Session(engine) as session:
        session.add(book)
        session.commit()
        session.refresh(book)
        return book
    
def get_book_by_id(engine, book_id):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        return book
    
def get_all_books(engine):
    with Session(engine) as session:
        books = session.exec(select(Book)).all()
        return books
    
def delete_book(engine, book_id):
    with Session(engine) as session:
        book = session.get(Book, book_id)
        if book:
            session.delete(book)
            session.commit()
            return True
        return False

def update_book(engine, old_book, updated_book):
    with Session(engine) as session:
        old_book.title = updated_book.title
        old_book.author = updated_book.author
        old_book.description = updated_book.description
        session.add(old_book)
        session.commit()
        session.refresh(old_book)
    return old_book
    