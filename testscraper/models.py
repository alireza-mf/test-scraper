from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

from scrapy.utils.project import get_project_settings


Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get('CONNECTION_STRING'))

def create_laptops_table(engine):
    """"""
    Base.metadata.create_all(engine)

class LaptopsDB(Base):
    """Sqlalchemy Laptops model"""
    __tablename__ = "Laptops"

    id = Column(Integer, primary_key=True)
    title = Column('title', String, nullable=True)
    image = Column('image', String, nullable=True)
    description = Column('description', String, nullable=True)
    price = Column('price', String, nullable=True)
