from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase
from src.core.config import DATABASE_URL
class Base(DeclarativeBase):
    pass

engine = create_engine(
    DATABASE_URL,
    echo=False,          # True — логирует SQL (для отладки)
    pool_pre_ping=True   # проверяет соединение
)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
