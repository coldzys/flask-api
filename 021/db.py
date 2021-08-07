import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

PATH = "./021/databases/"

engine = sqlalchemy.create_engine('sqlite:///./021/databases/db.sqlite')
base = declarative_base()
