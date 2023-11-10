from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


URL_PSQL_DATABASE = 'postgresql://postgres:badsha@localhost:5432/xpay_db'

engine_psql = create_engine(URL_PSQL_DATABASE)

SessionLocalPsql = sessionmaker(autocommit=False, autoflush=True,bind=engine_psql)

Base_Psql = declarative_base
