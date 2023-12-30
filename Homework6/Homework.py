# Необходимо создать базу данных для интернет-магазина. База данных должна
# состоять из трех таблиц: товары, заказы и пользователи. Таблица товары должна
# содержать информацию о доступных товарах, их описаниях и ценах. Таблица
# пользователи должна содержать информацию о зарегистрированных
# пользователях магазина. Таблица заказы должна содержать информацию о
# заказах, сделанных пользователями.
# ○ Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.
# ○ Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
# ○ Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.
# Создайте модели pydantic для получения новых данных и
# возврата существующих в БД для каждой из трёх таблиц
# (итого шесть моделей).
# Реализуйте CRUD операции для каждой из таблиц через
# создание маршрутов, REST API (итого 15 маршрутов).
# ○ Чтение всех
# ○ Чтение одного
# ○ Запись
# ○ Изменение
# ○ Удаление
import datetime
import random

from fastapi import FastAPI
import databases
from sqlalchemy import create_engine, select, update, delete, insert
from model import UsersIn, UsersOut, ItemOut, ItemIn, OrderOut, OrderIn
from sqla import Base, User, Item, Order


DATABASE_URL = "sqlite:///shop.sqlite"
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


@app.get("/")
async def index():
    users = await database.fetch_all(select(User))
    users = [user for user in users]
    orders = await database.fetch_all(select(Order))
    orders = [order for order in orders]
    items = await database.fetch_all(select(Item))
    items = [item for item in items]
    return {"Пользователи": users, "Товары": items, "Заказы": orders}


# _____________________________________________________________
@app.post("/users/")
async def create_user(new_user: UsersIn):
    new_user = insert(User).values(**new_user.model_dump())
    await database.execute(new_user)
    return {'Create user': 'ok'}


@app.get("/users/{user_id}/", response_model=UsersOut)
async def get_user(user_id: int):
    user = select(User).where(User.id == user_id)
    return await database.fetch_one(user)


@app.put("/users/{user_id}/", response_model=UsersOut)
async def update_user(user_id: int, new_user: UsersIn):
    update_user = update(User).where(User.id == user_id).values(**new_user.model_dump())
    await database.execute(update_user)
    return {'Update user': 'ok'}


@app.delete("/users/{user_id}/", response_model=UsersOut)
async def delete_user(user_id: int):
    delete_user = delete(User).where(User.id == user_id)
    await database.execute(delete_user)
    return {'Delete user': 'ok'}


# _____________________________________________________________
@app.post("/items/")
async def create_item(new_item: ItemIn):
    new_item = insert(Item).values(**new_item.model_dump())
    await database.execute(new_item)
    return {'Create item': 'ok'}


@app.get("/items/{item_id}/", response_model=ItemOut)
async def get_item(item_id: int):
    item = select(Item).where(Item.id == item_id)
    return await database.fetch_one(item)


@app.put("/items/{item_id}/", response_model=ItemOut)
async def update_item(item_id: int, new_item: ItemIn):
    update_item = update(Item).where(Item.id == item_id).values(**new_item.model_dump())
    await database.execute(update_item)
    return {'Update item': 'ok'}


@app.delete("/items/{item_id}/", response_model=ItemOut)
async def delete_item(item_id: int):
    delete_item = delete(Item).where(Item.id == item_id)
    await database.execute(delete_item)
    return {'Delete item': 'ok'}


# _____________________________________________________________
@app.post("/orders/")
async def create_order(new_order: OrderIn):
    new_order = insert(Order).values(**new_order.model_dump())
    await database.execute(new_order)
    return {'Create order': 'ok'}


@app.get("/orders/{order_id}/", response_model=OrderOut)
async def get_order(order_id: int):
    order = select(Order).where(Order.id == order_id)
    return await database.fetch_one(order)


@app.put("/orders/{order_id}/", response_model=OrderOut)
async def update_order(order_id: int, new_order: OrderIn):
    update_order = update(Order).where(Order.id == order_id).values(**new_order.model_dump())
    await database.execute(update_order)
    return {'Update order': 'ok'}


@app.delete("/orders/{order_id}/", response_model=OrderOut)
async def delete_order(order_id: int):
    delete_order = delete(Order).where(Order.id == order_id)
    await database.execute(delete_order)
    return {'Delete order': 'ok'}


@app.post('/fill')
async def fill():
    for i in range(10):
        await database.fetch_one(insert(User).values(name=f'user{i}', last_name=f'user{i}', email=f'user{i}@mail', password='123456'))
        await database.fetch_one(insert(Item).values(title=f'item{i}', description=f'item{i}', price=i*50))
    for i in range(10):
        await database.fetch_one(insert(Order).values(id_user=random.randint(1,11), id_item=random.randint(1,10), date= datetime.date(),status='OK'))