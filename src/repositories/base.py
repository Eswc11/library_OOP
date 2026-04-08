from sqlalchemy.orm import Session

class BaseRepository:
    model = None

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(self.model).all()

    def get_by_id(self, obj_id: int):
        return self.db.query(self.model).filter(self.model.id == obj_id).first()

    def delete(self, obj_id: int):
        db_obj = self.get_by_id(obj_id)
        if not db_obj:
            return None
        self.db.delete(db_obj)
        self.db.commit()
        return db_obj
