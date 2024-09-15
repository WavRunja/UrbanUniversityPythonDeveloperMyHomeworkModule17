from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.db import Base


# В модуле user.py создайте модель User, наследованную от ранее написанного Base со следующими атрибутами:
# __tablename__ = 'users'
class User(Base):
    __tablename__ = 'users'

    # id - целое число, первичный ключ, с индексом.
    id = Column(Integer, primary_key=True, index=True)
    # username - строка.
    username = Column(String, unique=True, index=True)
    # firstname - строка.
    firstname = Column(String)
    # lastname - строка.
    lastname = Column(String)
    # age - целое число.
    age = Column(Integer)
    # slug - строка, уникальная, с индексом.
    slug = Column(String, unique=True, index=True)

    # tasks - объект связи с таблицей с таблицей Task, где back_populates='user'.
    tasks = relationship("Task", back_populates="user")
