from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from models.user import User
from backend.db import SessionLocal
from schemas import CreateUser

router = APIRouter(
    prefix="/user",
    tags=["user"]
)


# Получаем сессию базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# В модуле user.py напишите APIRouter с префиксом '/user' и тегом 'user',
# а также следующие маршруты, с пустыми функциями:
# get '/' с функцией all_users.
@router.get("/")
async def all_users():
    # pass
    return {"message": "All users"}


# get '/user_id' с функцией user_by_id.
@router.get("/user_id")
async def user_by_id(user_id: int):
    # pass
    return {"message": f"User {user_id}"}


# post '/create' с функцией create_user.
@router.post("/create")
async def create_user(user: CreateUser, db: Session = Depends(get_db)):
    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=user.username.lower()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


# put '/update' с функцией update_user.
@router.put("/update")
async def update_user():
    # pass
    return {"message": "User updated"}


# delete '/delete' с функцией delete_user.
@router.delete("/delete")
async def delete_user():
    # pass
    return {"message": "User deleted"}
