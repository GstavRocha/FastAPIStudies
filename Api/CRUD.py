from sqlalchemy.orm import Session
from . import schemas, model
def getUser(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id_usuario == user_id).first()
def getGenero(db: Session,  genero: str):
    return db.query(model.User).filter(model.User.genero_usuario == genero).first()
def getNome(db: Session, name: str): ### aqui é um get
    return db.query(model.User).filter(model.User.nome_usuario == name).first()
def getTodos(db: Session, skip: int= 0, limit=100):
    return db.query(model.User).offset(skip).limit(limit).all()
def getView(db: Session, view: schemas.VwUser):
    return  db.query(model.ViewUser).select_from(model.ViewUser == view).all()
def create_user(db: Session, user: schemas.NameUser):
    db_user = model.User(nome_usuario = user.nome_usuario)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user