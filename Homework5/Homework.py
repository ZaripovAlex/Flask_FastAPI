from fastapi import FastAPI, Request
from Homework5.model import Music
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
music_list: list[Music] = []
templates = Jinja2Templates(directory="templates")

def fill_music_list():
    music_list.append(Music(id=1, artist="Bob Dylan", title="Like a Rolling Stone", album="Highway 61 Revisited", year= 1965))
    music_list.append(Music(id=2, artist="The Rolling Stones", title="Satisfaction", album="Out of Our Heads", year=1965))
    music_list.append(Music(id=3, artist="Джон Леннон", title="Imagine", album="Imagine", year=1971))
    music_list.append(Music(id=4, artist="Марвин Гэй", title="	What’s Going On", album="What’s Going On", year=1971))
    music_list.append(Music(id=5, artist="Арета Франклин", title="Respect", album=" I Never Loved a Man the Way I Love You", year=1967))
    music_list.append(Music(id=6, artist="The Beach Boys", title="Good Vibrations", album="Album 1", year=1966))
    music_list.append(Music(id=7, artist="Чак Берри", title="Johnny B. Goode", album="Chuck Berry Is on Top", year=1958))
    music_list.append(Music(id=8, artist="The Beatles", title="Hey Jude", album="Сингл The Beatles", year=1968))
    music_list.append(Music(id=9, artist="Nirvana", title="Smells Like Teen Spirit", album="Nevermind", year=1991))
    music_list.append(Music(id=10, artist="Рэй Чарльз", title="What’d I Say", album=" What’d I Say", year=1959))

@app.get("/" , response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "music_list": music_list})
# @app.get("/")
# async def root():
#     return music_list

@app.post("/music")
async def create_music(music: Music):
    music_list.append(music)
    return {'message': 'Music added successfully', 'music': music}

@app.post("/music/fill/")
async def fill_music():
    fill_music_list()
    return {'message': 'Music list filled successfully', 'music_list': music_list}
@app.put("/music/{music_id}")
async def update_music(music_id: int, new_music: Music):
    filtered_music_list = [music for music in music_list if music.id == music]
    if not filtered_music_list:
        return {'message': f'Music with id {music_id} not found'}
    music = filtered_music_list[0]
    music.id = new_music.id
    music.artist = new_music.artist
    music.title = new_music.title
    music.album = new_music.album
    music.year = new_music.year
    return {'message': 'Music updated successfully','music': music}

@app.delete("/music/{music_id}")
async def delete_music(music_id: int):
    filtered_music_list = [music for music in music_list if music.id == music_id]
    if not filtered_music_list:
        return {'message': f'Music with id {music_id} not found'}
    music = filtered_music_list[0]
    music_list.remove(music)
    return {'message': 'Music deleted successfully', 'music': music}


