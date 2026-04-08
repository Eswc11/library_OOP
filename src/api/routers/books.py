from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.dependencies import get_db
from src.schemas.books import BookCreate, BookRead, BookUpdate
from src.repositories.books import BookRepository

router = APIRouter(prefix="/books", tags=["books"])

@router.get("/", response_model=list[BookRead])
def read_books(db: Session = Depends(get_db)):
    repo = BookRepository(db)
    return repo.get_all()

@router.get("/{book_id}", response_model=BookRead)
def get_book(book_id: int, db: Session = Depends(get_db)):
    repo = BookRepository(db)
    book = repo.get_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("/", response_model=BookRead)
def create_book(book: BookCreate, db: Session = Depends(get_db)):
    repo = BookRepository(db)
    return repo.create(book)

@router.delete("/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    repo = BookRepository(db)
    success = repo.delete(book_id)
    if not success:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"message": f"Book {book_id} deleted"}

@router.patch("/{book_id}", response_model=BookRead)
def update_book(book_id: int, book_update: BookUpdate, db: Session = Depends(get_db)):
    repo = BookRepository(db)
    book = repo.update(book_id, book_update)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book
