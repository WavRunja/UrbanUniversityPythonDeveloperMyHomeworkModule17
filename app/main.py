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
