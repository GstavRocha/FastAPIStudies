from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from Api import CRUD, model, schemas
from Api.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.NameUser, db: Session = Depends(get_db)):
    db_user = CRUD.getNome(db,name = user.nome_usuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Nome Já cadastrado")
    return CRUD.create_user(db=db , user=user)

@app.get("/users/", response_model=list[schemas.User])
def getTodos(skip: int = 0 , limit: int = 100, db: Session = Depends(get_db)):
    users = CRUD.getTodos(db, skip=skip, limit=limit)
    return users
@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = CRUD.getUser(db, user_id= user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Usuario nao encontrado")
    return db_user
@app.get("/users/view", response_model=schemas.VwUser)
def read_view(db: Session= Depends(get_db)):
    user_view = CRUD.getView(db)
    return user_view




