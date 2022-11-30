import databases
import ormar
import sqlalchemy
from config import SQLALCHEMY_DB_URL

metadata = sqlalchemy.MetaData()
database = databases.Database(SQLALCHEMY_DB_URL)
engine = sqlalchemy.create_engine(SQLALCHEMY_DB_URL)


class MainMata(ormar.ModelMeta):
    metadata = metadata
    database = database