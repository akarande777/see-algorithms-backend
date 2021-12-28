from sqlalchemy import Column, DateTime, ForeignKey, Integer, Table, Text, Boolean, UniqueConstraint, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import PrimaryKeyConstraint

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)
    display_name = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, server_default=text("now()"))
    last_login = Column(DateTime)
    login_count = Column(Integer, nullable=False)


class Algorithm(Base):
    __tablename__ = 'algorithms'
    algo_id = Column(Integer, primary_key=True)
    algo_name = Column(Text, nullable=False, unique=True)


class Category(Base):
    __tablename__ = 'categories'
    cat_id = Column(Integer, primary_key=True)
    cat_name = Column(Text, nullable=False, unique=True)
    algorithms = relationship('Algorithm', secondary='algo_cat_map')


algo_cat_map = Table(
    'algo_cat_map',
    Base.metadata,
    Column('algo_id', ForeignKey('algorithms.algo_id'), nullable=False),
    Column('cat_id', ForeignKey('categories.cat_id'), nullable=False),
    UniqueConstraint('algo_id', 'cat_id')
)


class UserAlgoData(Base):
    __tablename__ = "user_algo_data"
    __table_args__ = (
        PrimaryKeyConstraint('user_id', 'algo_id'),
    )
    user_id = Column(ForeignKey('users.user_id'), nullable=False)
    algo_id = Column(ForeignKey('algorithms.user_id'), nullable=False)
    algo_data = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, server_default=text("now()"))
    active = Column(Boolean, nullable=False, server_default=text("true"))
