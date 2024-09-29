from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from models.user import User
from schemas import CreateUser, UpdateUser
from sqlalchemy import select, insert, update, delete
from slugify import slugify
from typing import Annotated

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# Получение всех пользователей
@router.get("/")
async def all_users(db: Annotated[Session, Depends(get_db)]):
    query = select(User)
    result = db.scalars(query).all()
    return result


# Получение пользователя по ID
@router.get("/{user_id}")
async def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    user = db.scalars(query).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


# Создание нового пользователя
@router.post("/create")
async def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    # Проверка на существование пользователя с таким username
    query = select(User).where((User.username == user.username) | (User.id == user.id))
    existing_user = db.scalars(query).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User with this username or ID already exists")

    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


# Обновление данных пользователя
@router.put("/update/{user_id}")
async def update_user(user_id: int, updated_user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    existing_user = db.scalars(query).first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(
        update(User)
        .where(User.id == user_id)
        .values(
            firstname=updated_user.firstname,
            lastname=updated_user.lastname,
            age=updated_user.age
        )
    )
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update is successful!'
    }


# Удаление пользователя
@router.delete("/delete/{user_id}")
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    query = select(User).where(User.id == user_id)
    existing_user = db.scalars(query).first()
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.execute(delete(User).where(User.id == user_id))
    db.commit()

    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User deleted successfully!'
    }
