from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.config_db import PostgresConfig

url = PostgresConfig.url
engine = create_engine(url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
