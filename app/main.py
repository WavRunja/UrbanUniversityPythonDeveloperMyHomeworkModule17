# Домашнее задание по теме "Структура проекта. Маршруты и модели Pydantic."
# Цель: усвоить основные правила структурирования проекта с использованием FastAPI.
# Начать написание небольшого "API" для менеджмента задач пользователей.

# Задача "Основные маршруты".
from fastapi import FastAPI
from routers import task, user

# В файле main.py создайте сущность FastAPI(),
app = FastAPI()


# напишите один маршрут для неё - '/',
# по которому функция возвращает словарь - {"message": "Welcome to Taskmanager"}.
@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}

# Импортируйте объекты APIRouter и подключите к ранее созданному приложению FastAPI,
# объединив все маршруты в одно приложение.
app.include_router(user.router)
app.include_router(task.router)

# [
#   {
#     "lastname": "Technique",
#     "id": 1,
#     "username": "user1",
#     "age": 40,
#     "firstname": "Pasha",
#     "slug": "user1"
#   },
#   {
#     "lastname": "Grylls",
#     "id": 3,
#     "username": "user3",
#     "age": 50,
#     "firstname": "Bear",
#     "slug": "user3"
#   }
# ]

# INFO:     Will watch for changes in these directories: ['E:\\PythonProjects\\app']
# INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
# INFO:     Started reloader process [9528] using StatReload
# INFO:     Started server process [9536]
# INFO:     Waiting for application startup.
# INFO:     Application startup complete.
# INFO:     127.0.0.1:57872 - "GET /docs HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57872 - "GET /openapi.json HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57882 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57882 - "GET / HTTP/1.1" 200 OK
# INFO:     127.0.0.1:57887 - "GET / HTTP/1.1" 200 OK
# 2024-09-20 09:06:12,275 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:06:12,292 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# 2024-09-20 09:06:12,292 INFO sqlalchemy.engine.Engine [generated in 0.00224s] ()
# 2024-09-20 09:06:12,304 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:57888 - "GET /user/ HTTP/1.1" 200 OK
# 2024-09-20 09:06:25,664 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:06:25,664 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:06:25,684 INFO sqlalchemy.engine.Engine [generated in 0.01385s] (0,)
# 2024-09-20 09:06:25,693 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:57892 - "GET /user/user_id?user_id=0 HTTP/1.1" 404 Not Found
# 2024-09-20 09:06:32,447 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:06:32,448 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:06:32,448 INFO sqlalchemy.engine.Engine [cached since 6.776s ago] (1,)
# 2024-09-20 09:06:32,449 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:57896 - "GET /user/user_id?user_id=1 HTTP/1.1" 404 Not Found
# 2024-09-20 09:10:07,182 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:10:07,190 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.username = ?
# 2024-09-20 09:10:07,190 INFO sqlalchemy.engine.Engine [generated in 0.00083s] ('user1',)
# 2024-09-20 09:10:07,200 INFO sqlalchemy.engine.Engine INSERT INTO users (username, firstname, lastname, age, slug) VALUES (?, ?, ?, ?, ?)
# 2024-09-20 09:10:07,200 INFO sqlalchemy.engine.Engine [generated in 0.00119s] ('user1', 'Pasha', 'Technique', 40, 'user1')
# 2024-09-20 09:10:07,208 INFO sqlalchemy.engine.Engine COMMIT
# 2024-09-20 09:10:07,218 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:10:07,220 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:10:07,220 INFO sqlalchemy.engine.Engine [generated in 0.00058s] (1,)
# 2024-09-20 09:10:07,220 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:59147 - "POST /user/create HTTP/1.1" 200 OK
# 2024-09-20 09:11:22,333 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:11:22,334 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.username = ?
# 2024-09-20 09:11:22,335 INFO sqlalchemy.engine.Engine [cached since 75.15s ago] ('user2',)
# 2024-09-20 09:11:22,339 INFO sqlalchemy.engine.Engine INSERT INTO users (username, firstname, lastname, age, slug) VALUES (?, ?, ?, ?, ?)
# 2024-09-20 09:11:22,340 INFO sqlalchemy.engine.Engine [cached since 75.14s ago] ('user2', 'Roza', 'Syabitova', 62, 'user2')
# 2024-09-20 09:11:22,343 INFO sqlalchemy.engine.Engine COMMIT
# 2024-09-20 09:11:22,348 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:11:22,348 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:11:22,348 INFO sqlalchemy.engine.Engine [cached since 75.13s ago] (2,)
# 2024-09-20 09:11:22,348 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:59164 - "POST /user/create HTTP/1.1" 200 OK
# 2024-09-20 09:12:20,555 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:12:20,555 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.username = ?
# 2024-09-20 09:12:20,555 INFO sqlalchemy.engine.Engine [cached since 133.4s ago] ('user3',)
# 2024-09-20 09:12:20,555 INFO sqlalchemy.engine.Engine INSERT INTO users (username, firstname, lastname, age, slug) VALUES (?, ?, ?, ?, ?)
# 2024-09-20 09:12:20,558 INFO sqlalchemy.engine.Engine [cached since 133.4s ago] ('user3', 'Alex', 'Unknown', 25, 'user3')
# 2024-09-20 09:12:20,561 INFO sqlalchemy.engine.Engine COMMIT
# 2024-09-20 09:12:20,582 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:12:20,582 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:12:20,582 INFO sqlalchemy.engine.Engine [cached since 133.4s ago] (3,)
# 2024-09-20 09:12:20,582 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:59187 - "POST /user/create HTTP/1.1" 200 OK
# 2024-09-20 09:12:32,191 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:12:32,192 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# 2024-09-20 09:12:32,192 INFO sqlalchemy.engine.Engine [cached since 379.9s ago] ()
# 2024-09-20 09:12:32,194 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:59191 - "GET /user/ HTTP/1.1" 200 OK
# 2024-09-20 09:13:51,716 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:13:51,717 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:13:51,725 INFO sqlalchemy.engine.Engine [cached since 446.1s ago] (3,)
# 2024-09-20 09:13:51,729 INFO sqlalchemy.engine.Engine UPDATE users SET firstname=?, lastname=?, age=? WHERE users.id = ?
# 2024-09-20 09:13:51,729 INFO sqlalchemy.engine.Engine [generated in 0.00077s] ('Bear', 'Grylls', 50, 3)
# 2024-09-20 09:13:51,729 INFO sqlalchemy.engine.Engine COMMIT
# INFO:     127.0.0.1:59196 - "PUT /user/update?user_id=3 HTTP/1.1" 200 OK
# 2024-09-20 09:14:07,767 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:14:07,769 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# 2024-09-20 09:14:07,770 INFO sqlalchemy.engine.Engine [cached since 475.5s ago] ()
# 2024-09-20 09:14:07,771 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:59198 - "GET /user/ HTTP/1.1" 200 OK
# 2024-09-20 09:14:49,937 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:14:49,938 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# WHERE users.id = ?
# 2024-09-20 09:14:49,938 INFO sqlalchemy.engine.Engine [cached since 504.3s ago] (2,)
# 2024-09-20 09:14:49,940 INFO sqlalchemy.engine.Engine DELETE FROM users WHERE users.id = ?
# 2024-09-20 09:14:49,941 INFO sqlalchemy.engine.Engine [generated in 0.00093s] (2,)
# 2024-09-20 09:14:49,943 INFO sqlalchemy.engine.Engine COMMIT
# INFO:     127.0.0.1:59201 - "DELETE /user/delete?user_id=2 HTTP/1.1" 200 OK
# 2024-09-20 09:14:58,218 INFO sqlalchemy.engine.Engine BEGIN (implicit)
# 2024-09-20 09:14:58,218 INFO sqlalchemy.engine.Engine SELECT users.id, users.username, users.firstname, users.lastname, users.age, users.slug
# FROM users
# 2024-09-20 09:14:58,218 INFO sqlalchemy.engine.Engine [cached since 525.9s ago] ()
# 2024-09-20 09:14:58,218 INFO sqlalchemy.engine.Engine ROLLBACK
# INFO:     127.0.0.1:59202 - "GET /user/ HTTP/1.1" 200 OK