import unittest
from flasgger import Swagger
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request, Blueprint
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.exceptions import NotFound
from config.settings import Config
from sqlalchemy.exc import IntegrityError
from urls import bp, index, about, transfer, addaccount, addpost
from app_blueprint.views import app_blueprint
from flasgger.utils import load_from_file
from flask_login import LoginManager
from models import db, Base, Customer, Transfer, Account
from auth import auth as auth_blueprint
app = Flask(__name__, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates', static_folder='static')
CORS(app)
app.config.from_object(Config)  # Assuming Config is imported from settings

# Access the database URI
db_uri = app.config['SQLALCHEMY_DATABASE_URI']
app.config['SECRET_KEY'] = 'keykeykey'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine = create_engine(db_uri)
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):

    return Customer.query.get(user_id)
# Bind the engine to the Base
Base.metadata.bind = engine

# Create a scoped session to handle database connections
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

# Access the Base for creating tables
Base.query = db_session.query_property()

app.register_blueprint(app_blueprint, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates')
app.register_blueprint(auth_blueprint)
db.init_app(app)
spec = load_from_file('C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/swagger.yaml')
swagger = Swagger(app, template=spec)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)