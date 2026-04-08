from pydantic import BaseModel
from src.schemas.books import BookRead

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    book_id: int | None = None

class UserRead(UserCreate):
    id: int
    book: BookRead | None = None
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    book_id: int | None = None
    
    class Config:
        from_attributes = True