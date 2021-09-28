import databases
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#============================
# 参考：https://fastapi.tiangolo.com/advanced/async-sql-databases/
#============================

DATABASE = 'postgresql'
USER =     'admin'
PASSWORD = 'password'
HOST =     '192.168.30.1'
PORT =     '5432'
DB_NAME =  'data_visualization'

# DATABASE_URL = "postgresql://user:password@postgresserver/db"
SQLALCHEMY_DATABASE_URL = f'{DATABASE}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'

# databases
# database = databases.Database(SQLALCHEMY_DATABASE_URL, min_size=5, max_size=20)

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# モデルクラスを作る(テーブル定義)
# models.pyでBaseを継承してテーブルの定義を行う
Base = declarative_base()