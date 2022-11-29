import databases
import ormar
import sqlalchemy


metadata = sqlalchemy.MetaData()
database = databases.Database("sqlite:///sqlite.db")


class MainMata(ormar.ModelMeta):
    metadata = metadata
    database = database