# app/views.py
from flask import Blueprint, jsonify, request, render_template
from flask import render_template, jsonify, request, Blueprint
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from models import db_session, Customer, Transfer, Account

# Create a Blueprint instance
app_blueprint = Blueprint('app_blueprint', __name__)

@app_blueprint.route('/index')
def index():
    posts = Transfer.query.order_by(Transfer.id.desc()).all()
    posts2 = Customer.query.order_by(Customer.id.desc()).all()
    return render_template('index.html', posts=posts, posts2=posts2)

@app_blueprint.route('/about')
def about():
    return render_template('about.html')

@app_blueprint.route('/post/<int:post_id>')
def transfer(post_id):
    try:
        post = Transfer.query.filter_by(id=post_id).one()
        post2 = Customer.query.filter_by(id=post_id).one()
        return render_template('post.html', post=post, post2=post2)
    except NotFound as e:
        return jsonify({'error': str(e)}), 404

@app_blueprint.route('/add')
def add():
    return render_template('add.html')

@app_blueprint.route('/account')
def account():
    return render_template('register.html')

@app_blueprint.route('/addaccount', methods=['POST'])
def addaccount():
    try:
        customerName = request.form['customerName']
        balance = request.form['balance']
        currencyCode = request.form['currencyCode']

        post1 = Account(customerName=customerName, balance=balance, currencyCode=currencyCode)
        if not customerName or not balance:
            return jsonify({'error': 'Invalid request. Please provide a customerName and balance.'}), 400

        db_session.add(post1)
        db_session.commit()

        return jsonify({'message': 'Item added to basket successfully'}), 201
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except IntegrityError as e:
        db_session.rollback()
        return jsonify({'error': 'Invalid request. One or more accounts do not exist.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app_blueprint.route('/addpost', methods=['POST'])
def addpost():
    try:
        currencyCode = request.form['currencyCode']
        amount = request.form['amount']
        fromAccountId = request.form['fromAccountId']
        toAccountId = request.form['toAccountId']

        post = Transfer(currencyCode=currencyCode, amount=amount, fromAccountId=fromAccountId, toAccountId=toAccountId)
        if not currencyCode or not amount:
            return jsonify({'error': 'Invalid request. Please provide a currencyCode and amount.'}), 400

        db_session.add(post)
        db_session.commit()

        return jsonify({'message': 'Item added to basket successfully'}), 201
    except NotFound as e:
        return jsonify({'error': str(e)}), 404
    except IntegrityError as e:
        db_session.rollback()
        return jsonify({'error': 'Invalid request. One or more accounts do not exist.'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500
