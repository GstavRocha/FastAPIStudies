from sqlalchemy.orm import Session
from . import schemas, model
def getUser(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id_usuario == user_id).first()
def getGenero(db: Session,  genero: str):
    return db.query(model.User).filter(model.User.genero_usuario == genero).first()
def getNome(db: Session, name: str):
    return db.query(model.User).filter(model.User.nome_usuario == name).first()
def getTodos(db: Session, skip: int= 0, limit=100):
    return db.query(model.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.createUser, name: str, genero: str):
    db_user = model.User(name = user.name, genero = user.genero) ##corrigir
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = model.Item(**item.dict(), id =user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item