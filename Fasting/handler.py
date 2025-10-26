from sqlalchemy import create_engine
from sqlalchemy.dialects.sqlite import *

SQLALCHEMY_DATABASE_URL = "sqlite://./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
