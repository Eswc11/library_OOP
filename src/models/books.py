from sqlalchemy import Column, Integer, String, Date, func
from sqlalchemy.orm import relationship
from src.core.database import Base

class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    date = Column(Date, server_default=func.current_date())
    users = relationship("User", back_populates="book")


