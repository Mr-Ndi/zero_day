from sqlmodel import Session, select
from models.book_model import Book

async def insert_book(engine, book):
    async with Session(engine) as session:
        session.add(book)
        await session.commit()
        await session.refresh(book)
        return book
    
async def get_book_by_id(engine, book_id):
    async with Session(engine) as session:
        book = await session.get(Book, book_id)
        return book
    
async def get_all_books(engine):
    async with Session(engine) as session:
        books = await session.exec(select(Book)).all()
        return books
    
async def delete_book(engine, book_id):
    async with Session(engine) as session:
        book = await session.get(Book, book_id)
        if book:
            await session.delete(book)
            await session.commit()
            return True
        return False

async def update_book(engine, old_book, updated_book):
    async with Session(engine) as session:
        old_book.title = updated_book.title
        old_book.author = updated_book.author
        old_book.description = updated_book.description
        session.add(old_book)
        await session.commit()
        await session.refresh(old_book)
    return old_book
    