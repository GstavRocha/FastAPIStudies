from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from Api import CRUD, model, schemas
from Api.database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)
app = FastAPI()
