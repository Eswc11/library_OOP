from src.models.books import Book
from src.schemas.books import BookCreate, BookUpdate
from src.repositories.base import BaseRepository

class BookRepository(BaseRepository):
    model = Book

    def create(self, book_data: BookCreate):
        db_book = self.model(**book_data.model_dump())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def update(self, book_id: int, book_update: BookUpdate):
        db_book = self.get_by_id(book_id)
        if not db_book:
            return None
        
        update_data = book_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_book, key, value)
        
        self.db.commit()
        self.db.refresh(db_book)
        return db_book
