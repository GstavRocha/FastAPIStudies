from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import  relationship

from .database import Base

class User(Base):
    __tablename__ = "tb_usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String)
    genero_usuario = Column(Enum('F', 'M'))