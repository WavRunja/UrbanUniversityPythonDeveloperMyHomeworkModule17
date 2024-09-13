from fastapi import APIRouter

router = APIRouter(
    prefix="/task",
    tags=["task"]
)


# В модуле task.py напишите APIRouter с префиксом '/task' и тегом 'task',
# а также следующие маршруты, с пустыми функциями:
# get '/' с функцией all_tasks.
@router.get("/")
async def all_tasks():
    # pass
    return {"message": "All tasks"}


# get '/task_id' с функцией task_by_id.
@router.get("/task_id")
async def task_by_id(task_id: int):
    # pass
    return {"message": f"Task {task_id}"}


# post '/create' с функцией create_task.
@router.post("/create")
async def create_task():
    # pass
    return {"message": "Task created"}


# put '/update' с функцией update_task.
@router.put("/update")
async def update_task():
    # pass
    return {"message": "Task updated"}


# delete '/delete' с функцией delete_task.
@router.delete("/delete")
async def delete_task():
    # pass
    return {"message": "Task deleted"}
