


from flask import Flask, render_template, jsonify, request, Blueprint
from werkzeug.exceptions import NotFound
from sqlalchemy.exc import IntegrityError
from urls import bp, index, about, transfer, add, account, addaccount, addpost
from app_blueprint.views import app_blueprint, db
app = Flask(__name__, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lasisa23$U@127.0.0.1:3306/money_transf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

app.register_blueprint(app_blueprint, template_folder='C:/Users/Acer/PycharmProjects/pythonProject/flask_money_transfer/appmt/templates')
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
