import datetime

from pydantic import BaseModel

class BookCreate(BaseModel):
    model_config = {"json_schema_extra": {"example": {
        "name": "Название книги",
        "author": "Автор"
    }}}
    name: str
    date: datetime.date | None = None

class BookRead(BookCreate):
    id: int
    class Config:
        from_attributes = True
class BookUpdate(BaseModel):
    name: str | None = None
    date: datetime.date | None = None
    class Config:
        from_attributes = True