
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.exceptions import NotFound
from config.settings import Config
from sqlalchemy.exc import IntegrityError
from urls import bp, index, about, transfer, add, account, addaccount, addpost
from app_blueprint.views import app_blueprint
from models import db, Base, Customer, Transfer, Account
app = Flask(__name__, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates', static_folder='static')

app.config.from_object(Config)  # Assuming Config is imported from settings

# Access the database URI
db_uri = app.config['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(db_uri)

# Bind the engine to the Base
Base.metadata.bind = engine

# Create a scoped session to handle database connections
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Access the Base for creating tables
Base.query = db_session.query_property()

app.register_blueprint(app_blueprint, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates')
db.init_app(app)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)
