from pydantic import  BaseModel
from enum import  Enum

class ItemBase(BaseModel):
    id: int
    nome_usuario: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    nome_usuario = str
    class Config:
        orm_mode = True

class createUser(ItemBase):
    nome_usuario: str
    class Config:
        orm_mode = True
class NameUser(BaseModel):
    nome_usuario: str


class User(NameUser):
    usuarios: list[Item] = []
    class Config:
       orm_mode = True

class VwUser(BaseModel):
    id_usuario = int
    nome_usuario = str
    genero = Enum("F","M")
    class Config:
        orm_mode = True