from sqlmodel import SQLModel, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from models.book_model import Book


def get_session_maker(engine):
    return sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def insert_book(engine, book):
    async_session_maker = get_session_maker(engine)
    async with async_session_maker() as session:
        db_book = Book.from_orm(book)
        session.add(db_book)
        await session.commit()
        await session.refresh(db_book)
        return db_book

async def get_book_by_id(engine, book_id):
    async_session_maker = get_session_maker(engine)
    async with async_session_maker() as session:
        book = await session.get(Book, book_id)
        return book
    
async def get_all_books(engine):
    async_session_maker = get_session_maker(engine)
    async with async_session_maker() as session:
        result = await session.execute(select(Book))
        books = result.scalars().all()
        return books
    
async def delete_book(engine, book_id):
    async_session_maker = get_session_maker(engine)
    async with async_session_maker() as session:
        book = await session.get(Book, book_id)
        if book:
            await session.delete(book)
            await session.commit()
            return True
        return False

async def update_book(engine, old_book, updated_book):
    async_session_maker = get_session_maker(engine)
    async with async_session_maker() as session:
        old_book.title = updated_book.title
        old_book.author = updated_book.author
        old_book.description = updated_book.description
        session.add(old_book)
        await session.commit()
        await session.refresh(old_book)
    return old_book
    