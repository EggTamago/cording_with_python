from typing import List

import databases
import  sqlalchemy

#============================
# 参考：https://fastapi.tiangolo.com/advanced/async-sql-databases/
#============================

DATABASE = 'mydb'
USER = 'admin'
PASSWORD = 'password'
HOST = '192.168.30.1'
PORT = '5432'
DB_NAME = 'mydb'

# DATABASE_URL = "postgresql://user:password@postgresserver/db"
DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

# databases
database = databases.Database(DATABASE_URL, min_size=5, max_size=20)

ECHO_LOG = False
engine = sqlalchemy.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata = sqlalchemy.MetaData()