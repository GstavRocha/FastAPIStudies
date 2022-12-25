from sqlalchemy import Column, Integer, String, Enum, DDL, event
from .database import Base


class User(Base):
    __tablename__ = "tb_usuario"
    id_usuario = Column(Integer, primary_key=True, index=True)
    nome_usuario = Column(String)

class ViewUser(Base):
    __tablename__ = "vw_usuario"
    id_usuario = Column(Integer, primary_key=True)
    nome_usuario = Column(String)
    genero = Column(Enum('F','M','N'))

viewTes = DDL(
    "SELECT id_usuario , nome_usuario , genero from tb_usuario;"
)

event.listen(User,"select",viewTes.execute_if(dialect="mysql"))