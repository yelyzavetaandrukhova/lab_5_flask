from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(255), nullable=False)
    emailAddress = db.Column(db.String(255), nullable=False)

class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(255), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    currencyCode = db.Column(db.String(10), nullable=False)

class Transfer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currencyCode = db.Column(db.String(10), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    fromAccountId = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    toAccountId = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)


