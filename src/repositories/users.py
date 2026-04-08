from sqlalchemy.orm import Session, joinedload
from src.models.users import User
from src.schemas.users import UserCreate, UserUpdate
from src.repositories.base import BaseRepository

class UserRepository(BaseRepository):
    model = User

    def get_all(self):
        # Переопределяем метод для загрузки связанных книг (Eager Loading)
        return self.db.query(self.model).options(joinedload(User.book)).all()

    def get_by_id(self, user_id: int):
        # Переопределяем метод для загрузки связанных книг
        return self.db.query(self.model).options(joinedload(User.book)).filter(User.id == user_id).first()

    def create(self, user_data: UserCreate):
        db_user = self.model(**user_data.model_dump())
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def update(self, user_id: int, user_update: UserUpdate):
        db_user = self.get_by_id(user_id)
        if not db_user:
            return None
        
        update_data = user_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_user, key, value)
        
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
