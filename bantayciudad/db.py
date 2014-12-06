__author__ = 'onvolo'
from sqlalchemy import Table, Column
from sqlalchemy import Integer, Numeric, String
from sqlalchemy.orm import scoped_session, session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

config = {
    "db": {
        "driver": "mysql+mysqldb",
        "username": "root",
        "password": "",
        "host": "localhost",
        "port": 3306,
        "database": "gateseer",
    }
}

engine = create_engine("%s://%s:%s@%s:%s/%s" % (
    config["db"]["driver"],
    config["db"]["username"],
    config["db"]["password"],
    config["db"]["host"],
    config["db"]["port"],
    config["db"]["database"]))
mysql_session = Session(bind=engine)
