from fastapi import APIRouter

router = APIRouter()

@router.get("/books")
async def books():
    return {"message": "List of books"}

@router.get("/book/{book_id}")
async def get_book(book_id: int):
    return {"message": f"Get details for book {book_id}"}

@router.post("/book")
async def create_book():
    return {"message": "Create a new book"}

@router.put("/book/{book_id}")
async def update_book(book_id: int):
    return {"message": f"Update book {book_id}"}

@router.delete("/book/{book_id}")
async def delete_book(book_id: int):
    return {"message": f"Delete book {book_id}"}