from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from models import db
from models import db_session, Customer, Transfer, Account
from flask_login import login_required, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    customerName = request.form.get('customerName')
    emailAddress = request.form.get('emailAddress')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Customer.query.filter_by(emailAddress=emailAddress).first()

    login_user(user = Customer(customerName=customerName, emailAddress=emailAddress), remember=remember)

    if user:
        # User with the given email address exists, log them in
        login_user(user)
        return redirect(url_for('auth.account'))

@auth.route('/add')
def add():
    if current_user.is_authenticated:
        user_id = current_user.id

    # Query transfers where fromAccountId or toAccountId is equal to user_id
        transfers = Transfer.query.filter((Transfer.fromAccountId == user_id) | (Transfer.toAccountId == user_id)).all()

        return render_template('add.html', transfers=transfers, user_id=user_id)
    else:
# Handle the case where the user is not logged in (anonymous)
        return render_template('add.html')

@auth.route('/account')
def account():
    if current_user.is_authenticated:
        password = current_user.password

        # Query transfers where fromAccountId or toAccountId is equal to user_id
        accounts = Account.query.filter(Account.currencyCode == password).all()

        return render_template('register.html', accounts=accounts, password=password)
    else:
        # Handle the case where the user is not logged in (anonymous)
        return render_template('register.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    customerName = request.form.get('customerName')
    emailAddress = request.form.get('emailAddress')
    password = request.form.get('password')

    user = Customer.query.filter_by(emailAddress=emailAddress).first()

    if user:
        flash('Email address already exists.')
        return redirect(url_for('auth.add'))

    new_user = Customer(customerName=customerName, emailAddress=emailAddress)

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.add'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('app_blueprint.index'))