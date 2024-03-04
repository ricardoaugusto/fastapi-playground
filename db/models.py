from db.database import Base
from sqlalchemy import Column, Integer, String

"""
SQLAlchemy Models

Definitions for database models or ORM (Object-Relational Mapping) entities.
These models represent the structure of your data in the database and are
used to interact with the database tables.
"""


class DbUser(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
