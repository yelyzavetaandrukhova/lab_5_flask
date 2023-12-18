# app/views.py
# app/views.py

from flask import Blueprint, jsonify, request, render_template
from flask import render_template, jsonify, request, Blueprint
from sqlalchemy.exc import IntegrityError
from werkzeug.exceptions import NotFound
from sqlalchemy.orm.exc import NoResultFound
from models import db_session, Customer, Transfer, Account
from flask_login import login_required, current_user

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

@app_blueprint.route('/post/<int:post_id>', methods=['POST','GET'])
def transfer(post_id):
        post = Transfer.query.filter_by(id=post_id).one()

        return render_template('post.html', post=post)


@app_blueprint.route('/addaccount', methods=['POST'])
def addaccount():
    try:
        customerName = request.form['customerName']
        balance = request.form['balance']
        currencyCode = request.form['currencyCode']

        account = Account(customerName=customerName, balance=balance, currencyCode=currencyCode)
        if not customerName or not balance:
            return jsonify({'error': 'Invalid request. Please provide a customerName and balance.'}), 400

        db_session.add(account)
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
# Update the route to accept both GET and POST methods
from flask import jsonify, render_template

@app_blueprint.route('/deletepost/<int:post_id>', methods=['GET', 'POST'])
def deletepost(post_id):
    if request.method == 'GET':
        # Render the confirmation page
        post = Transfer.query.get(post_id)
        return render_template('deletepost.html', post=post)

    elif request.method == 'POST':
        # Perform the delete operation
        try:
            with db_session.begin():
                post = Transfer.query.filter_by(id=post_id).first()
                db_session.delete(post)
                db_session.commit()
            return jsonify({"message": "Post was successfully deleted"})
        except NoResultFound:
            return jsonify({"error": "Post not found"}), 404
        except Exception as e:
            # Handle other exceptions (e.g., database connection issues)
            db_session.rollback()
            return jsonify({"error": f"An error occurred: {str(e)}"}), 500
        finally:
            db_session.close()
