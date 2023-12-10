from app import db
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, jsonify, request, Blueprint
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError

from views import app_blueprint

app = Flask(__name__, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lasisa23$U@127.0.0.1:3306/money_transf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.register_blueprint(app_blueprint, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
