from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from slugify import slugify
from sqlalchemy import select, update, delete
from sqlalchemy.orm import Session

from backend.db_depends import get_db
from models.task import Task
from models.user import User
from schemas import CreateTask, UpdateTask

router = APIRouter(
    prefix="/task",
    tags=["task"]
)


# В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task',
# а также следующие маршруты, с пустыми функциями:
# get '/' с функцией all_tasks.
@router.get("/")
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    query = select(Task)
    result = db.scalars(query).all()
    return result


# get '/task_id' с функцией task_by_id.
@router.get("/task_id")
async def task_by_id(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    task = db.scalars(query).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")
    return task


# post '/create' с функцией create_task.
@router.post("/create")
async def create_task(task: CreateTask, user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    user = db.scalars(query).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    new_task = Task(
        title=task.title,
        content=task.content,
        priority=task.priority,
        user_id=user_id,
        slug=slugify(task.title)
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful',
        'task': new_task
    }


# put '/update' с функцией update_task.
@router.put("/update/task_id")
async def update_task(task_id: int, updated_task: UpdateTask, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    task = db.scalars(query).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(
        update(Task)
        .where(Task.id == task_id)
        .values(
            title=updated_task.title,
            content=updated_task.content,
            priority=updated_task.priority
        )
    )
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update is successful!'
    }


# delete '/delete' с функцией delete_task.
@router.delete("/delete/task_id")
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(Task).where(Task.id == task_id)
    task = db.scalars(query).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task was not found")

    db.execute(delete(Task).where(Task.id == task_id))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task deleted successfully!'
    }

# По условию задачи:

# [
#   {
#     "title": "FirstTask",
#     "content": "Content1",
#     "completed": false,
#     "slug": "firsttask",
#     "priority": 0,
#     "id": 1,
#     "user_id": 1
#   },
#   {
#     "title": "SecondTask",
#     "content": "Content2",
#     "completed": false,
#     "slug": "secondtask",
#     "priority": 2,
#     "id": 2,
#     "user_id": 1
#   },
#   {
#     "title": "ThirdTask",
#     "content": "Content3",
#     "completed": false,
#     "slug": "thirdtask",
#     "priority": 4,
#     "id": 3,
#     "user_id": 3
#   },
#   {
#     "title": "FourthTask",
#     "content": "Content4",
#     "completed": false,
#     "slug": "fourthtask",
#     "priority": 6,
#     "id": 4,
#     "user_id": 3
#   }
# ]
