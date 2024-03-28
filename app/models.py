from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


class Note(BaseModel):
    title: str
    content: str
