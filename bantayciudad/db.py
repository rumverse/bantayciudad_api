__author__ = 'rumverse'
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
        "database": "bantayciudad",
    }
}
