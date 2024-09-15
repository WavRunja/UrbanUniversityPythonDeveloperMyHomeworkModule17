from sqlalchemy.schema import CreateTable
from models.user import User
from models.task import Task
from backend.db import engine

# SQL-запрос для создания таблицы пользователей
print(CreateTable(User.__table__).compile(engine))

# SQL-запрос для создания таблицы задач
print(CreateTable(Task.__table__).compile(engine))

# Вывод на консоль:

# CREATE TABLE users (
# 	id INTEGER NOT NULL,
# 	username VARCHAR,
# 	firstname VARCHAR,
# 	lastname VARCHAR,
# 	age INTEGER,
# 	slug VARCHAR,
# 	PRIMARY KEY (id)
# )


# CREATE TABLE tasks (
# 	id INTEGER NOT NULL,
# 	title VARCHAR,
# 	content VARCHAR,
# 	priority INTEGER,
# 	completed BOOLEAN,
# 	user_id INTEGER NOT NULL,
# 	slug VARCHAR,
# 	PRIMARY KEY (id),
# 	FOREIGN KEY(user_id) REFERENCES users (id)
# )
