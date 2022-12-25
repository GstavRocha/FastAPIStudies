from urllib.parse import quote_plus
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#
# password = urllib3('D@nidani1985')
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://gustavo:%s@localhost:3306/db_teste" % quote_plus("XXX")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker()
SessionLocal.configure(bind=engine)
Base = declarative_base()

