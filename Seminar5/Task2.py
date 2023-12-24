# Создать API для получения списка фильмов по жанру.
# Приложение должно иметь возможность получать список фильмов по заданному жанру.
# ● Создайте модуль приложения и настройте сервер и маршрутизацию.
# ● Создайте класс Movie с полями id, title, description и genre.
# ● Создайте список movies для хранения фильмов.
# ● Создайте маршрут для получения списка фильмов по жанру (метод GET).
# ● Реализуйте валидацию данных запроса и ответа.

from fastapi import FastAPI
from models import Movie

app = FastAPI()
movies: list[Movie] = []


@app.get("/")
async def index():
    return movies

@app.get("/{genre}")
async def get_movies_by_genre(genre: str):
    filtered_movies = [movie for movie in movies if movie.genre == genre]
    return filtered_movies

@app.post("/movies/")
async def create_movie(movie: Movie):
    movies.append(movie)
    return movie
