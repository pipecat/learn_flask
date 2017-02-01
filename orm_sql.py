from sqlqlchemy import create_engine, Column, Integer, String, Sequence
from sqlqlchemy.ext.declarative import  declarative_base
from sqlalchemy import and_, or_
from sqlalchemy.orm import sessionmaker

from mysql_consts import DB_URI

eng = create_engine(DB_URI)
Base = declarative_base()

class User(Base):
    __tablename__ = 'Users'

    id = Column(Integer, Sequence('user_id_seq'))