# Разработать API для управления списком пользователей с использованием базы данных SQLite.
# Для этого создайте модель User со следующими полями:
# - id: int (идентификатор пользователя, генерируется автоматически)
# - username: str (имя пользователя)
# - email: str (электронная почта пользователя)
# - password: str (пароль пользователя)
# API должно поддерживать следующие операции:
# - Получение списка всех пользователей: GET /users/
# - Получение информации о конкретном пользователе: GET /users/{user_id}/
# - Создание нового пользователя: POST /users/
# - Обновление информации о пользователе: PUT /users/{user_id}/
# - Удаление пользователя: DELETE /users/{user_id}/
#
# Для валидации данных используйте параметры Field модели User.
# Для работы с базой данных используйте SQLAlchemy и модуль databases.


from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, select, update, delete, insert
from models import UserIn, UserOut
from sqla import Base, User as SUsers

DATABASE_URL = "sqlite:///users.sqlite"
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
