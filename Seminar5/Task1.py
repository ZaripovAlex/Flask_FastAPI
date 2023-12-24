# Создать API для управления списком задач. Приложение должно иметь возможность создавать, обновлять, удалять и получать список задач.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Task с полями id, title, description и status.
# ● Создайте список tasks для хранения задач.
# ● Создайте маршрут для получения списка задач (метод GET).
# ● Создайте маршрут для создания новой задачи (метод POST).
# ● Создайте маршрут для обновления задачи (метод PUT).
# ● Создайте маршрут для удаления задачи (метод DELETE).
# ● Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from models import Task

app = FastAPI()
tasks: list[Task] = []
@app.get("/")
async def index():
    return tasks

@app.post("/task/")
async def create_task(task: Task):
    tasks.append(task)
    return task
@app.put("/task/{id}")
async def update_task(id: int, new_task: Task):
    filtered_tasks = [task for task in tasks if task.id == id]
    if not filtered_tasks:
        return {"message": "Task not found"}
    task = filtered_tasks[0]
    task.title = new_task.title
    task.description = new_task.description
    task.status = new_task.status
    return {"message": "Task updated successfully", "task": task}

@app.delete("/task/{id}")
async def delete_task(id: int):
    filtered_tasks = [task for task in tasks if task.id == id]
    if not filtered_tasks:
        return {"message": "Task not found"}
    task = filtered_tasks[0]
    tasks.remove(task)
    return {"message": "Task deleted successfully", "task": task}
