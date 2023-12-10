# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base
from flask_sqlalchemy import SQLAlchemy
Base = declarative_base()
db = SQLAlchemy()
from sqlalchemy.orm import sessionmaker, scoped_session
# Your existing model definitions here

# Assuming you have an engine defined (replace 'your_database_uri' with your actual URI)

# Bind the engine to the metadata


class Customer(Base):
    __tablename__ = 'Customer'
    id = Column(Integer, primary_key=True)
    customerName = Column(String(255), nullable=False)
    emailAddress = Column(String(255), nullable=False)


class Account(Base):
    __tablename__ = 'Account'
    id = Column(Integer, primary_key=True)
    customerName = Column(String(255), nullable=False)
    balance = Column(Integer, nullable=False)
    currencyCode = Column(String(10), nullable=False)


class Transfer(Base):
    __tablename__ = 'Transfer'
    id = Column(Integer, primary_key=True)
    currencyCode = Column(String(10), nullable=False)
    amount = Column(Integer, nullable=False)
    fromAccountId = Column(Integer, ForeignKey('Account.id'))
    toAccountId = Column(Integer, ForeignKey('Account.id'))
    from_account = relationship('Account', foreign_keys=[fromAccountId])
    to_account = relationship('Account', foreign_keys=[toAccountId])
engine = db.create_engine('mysql+pymysql://root:lasisa23$U@127.0.0.1:3306/money_transf')

# Create a session factory
Session = sessionmaker(bind=engine)
Base.metadata.bind = engine

# Create tables
Base.metadata.create_all(bind=engine)

# Create a scoped session
db_session = scoped_session(Session)