from fastapi import APIRouter
from middleware.schemas import BookCreate, BookUpdate
from controllers.book_controller import get_book, get_books, create_book, remove_book, modify_book

router = APIRouter()

@router.get("/books")
async def books():
    return await get_books()

@router.get("/book/{book_id}")
async def get_book(book_id: int):
    return await get_book(book_id=book_id)

@router.post("/book")
async def create_book(book: BookCreate):
    return await create_book(book=book)

@router.put("/book/{book_id}")
async def update_book(book_id: int, book: BookUpdate):
    return await modify_book(book_id=book_id, updated_book=book)

@router.delete("/book/{book_id}")
async def delete_book(book_id: int):
    return await remove_book(book_id=book_id)