from pydantic import BaseModel

class Music(BaseModel):
    id: int
    artist: str
    title: str
    album: str
    year: int


