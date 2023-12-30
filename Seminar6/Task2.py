# Создать веб-приложение на FastAPI, которое будет предоставлять API для работы с базой данных пользователей.
# Пользователь должен иметь следующие поля:
#
# - ID (автоматически генерируется при создании пользователя)
# - Имя (строка, не менее 2 символов)
# - Фамилия (строка, не менее 2 символов)
# - Дата рождения (строка в формате "YYYY-MM-DD")
# - Email (строка, валидный email)
# - Адрес (строка, не менее 5 символов)
#
# API должен поддерживать следующие операции:
#
# 1. Добавление пользователя в базу данных
# 2. Получение списка всех пользователей в базе данных
# 3. Получение пользователя по ID
# 4. Обновление пользователя по ID
# 5. Удаление пользователя по ID
#
# Приложение должно использовать базу данных SQLite3 для хранения пользователей.

from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, select, update, delete, insert
from models import UserIn, UserOut
from sqla import Base, Users2 as SUsers

DATABASE_URL = "sqlite:///users2.sqlite"
database = databases.Database(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/", response_model=list[UserIn])
async def index():
    users = select(SUsers)
    return await database.fetch_all(users)


@app.post("/users/")
async def create_user(user: UserIn):
    new_user = insert(SUsers).values(**user.model_dump())
    await database.execute(new_user)
    return {'Create user': 'ok'}


@app.get("/users/{user_id}/", response_model=UserOut)
async def get_user(user_id: int):
    user = select(SUsers).where(SUsers.id == user_id)
    return await database.fetch_one(user)


@app.put("/users/{user_id}/")
async def update_user(user_id: int, new_user: UserIn):
    update_user = update(SUsers).where(SUsers.id == user_id).values(**new_user.model_dump())
    await database.execute(update_user)
    return {'Update user': 'ok'}


@app.delete("/users/{user_id}/")
async def delete_user(user_id: int):
    delete_user = delete(SUsers).where(SUsers.id == user_id)
    await database.execute(delete_user)
    return {'Delete user': 'ok'}
