# Создать веб-страницу для отображения списка пользователей.
# Приложение должно использовать шаблонизатор Jinja для динамического формирования HTML страницы.
# Создайте модуль приложения и настройте сервер и маршрутизацию.
# Создайте класс User с полями id, name, email и password.
# Создайте список users для хранения пользователей.
# Создайте HTML шаблон для отображения списка пользователей.
# Шаблон должен содержать заголовок страницы, таблицу со списком пользователей и кнопку для добавления нового пользователя.
# Создайте маршрут для отображения списка пользователей (метод GET).
# Реализуйте вывод списка пользователей через шаблонизатор Jinja.


from fastapi import FastAPI, Request
from models import User
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

templates = Jinja2Templates(directory="templates")
app = FastAPI()
users: list[User] = []


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "users": users})


@app.post("/users/")
async def create_user(user: User):
    users.append(user)
    return user


@app.put("/users/{user_id}")
async def update_user(user_id: int, new_user: User):
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'message': 'user not found'}
    user = filtered_users[0]
    user.id = new_user.id
    user.name = new_user.name
    user.email = new_user.email
    user.password = new_user.password
    return {'message': 'user updated', 'user': user}


@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    filtered_users = [user for user in users if user.id == user_id]
    if not filtered_users:
        return {'message': 'user not found'}
    user = filtered_users[0]
    users.remove(user)
    return {'message': 'user deleted', 'user': user}
