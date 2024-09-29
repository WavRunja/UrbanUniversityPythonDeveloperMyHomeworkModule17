from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# База данных и движок:
# В модуле db.py:
# Импортируйте все необходимые функции и классы ,
# создайте движок указав пусть в БД - 'sqlite:///taskmanager.db' и локальную сессию (по аналогии с видео лекцией).
# SQLALCHEMY_DATABASE_URL = "sqlite:///taskmanager.db"
SQLALCHEMY_DATABASE_URL = "sqlite:///./taskmanager.db"


engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# Локальная сессия
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Создайте базовый класс Base для других моделей, наследуясь от DeclarativeBase.
class Base(DeclarativeBase):
    pass
