from pydantic import BaseModel, Field
from datetime import date

# Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY),
# имя, фамилия, адрес электронной почты и пароль.

class UsersOut(BaseModel):
    id: int = Field(primary_key=True)
    name: str
    last_name: str
    email: str
    password: str



class UsersIn(BaseModel):
    name: str
    last_name: str
    email: str
    password: str


# Таблица товаров должна содержать следующие поля: id (PRIMARY KEY),
# название, описание и цена.
class ItemOut(BaseModel):
    id: int = Field(primary_key=True)
    title: str
    description: str
    price: float


class ItemIn(BaseModel):
    title: str
    description: str
    price: float

# Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id
# пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус
# заказа.
class OrderOut(BaseModel):
    id: int = Field(primary_key=True)
    id_user: int = Field(foreign_key='users.id')
    id_item: int = Field(foreign_key='products.id')
    date: date
    status: str


class OrderIn(BaseModel):
    id_user: int = Field(foreign_key='users.id')
    id_item: int = Field(foreign_key='products.id')
    date: date
    status: str
