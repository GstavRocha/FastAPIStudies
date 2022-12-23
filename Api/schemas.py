from pydantic import  BaseModel

class ItemBase(BaseModel):
    id: int
    name: str
    genero: str

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    name: str
    genero: str
    class Config:
        orm_mode = True

class createUser(ItemBase):
    name: str
    genero: str
    class Config:
        orm_mode = True

class listUsers(createUser):
    id: int
    users: list[Item] =[]
    class Config:
       orm_mode = True