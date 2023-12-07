from flask import Flask, request, jsonify, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:lasisa23$U@127.0.0.1:3306/money_transf'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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
    fromAccountId = db.Column(db.Integer, ForeignKey('account.id'), nullable=False)
    toAccountId = db.Column(db.Integer, ForeignKey('account.id'), nullable=False)
@app.route('/index')
def index():
    posts = Transfer.query.order_by(Transfer.id.desc()).all()

    posts2 = Customer.query.order_by(Customer.id.desc()).all()
    return render_template('index.html', posts=posts, posts2=posts2)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def transfer(post_id):
    post = Transfer.query.filter_by(id=post_id).one()
    post2 = Customer.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post, post2=post2)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/account')
def account():
    return render_template('register.html')

@app.route('/addaccount', methods=['POST'])
def addaccount():
    id = request.form['id']
    customerName = request.form['customerName']
    balance = request.form['balance']
    currencyCode = request.form['currencyCode']

    post1 = Account(id=id, customerName=customerName, balance=balance,  currencyCode=currencyCode)

    db.session.add(post1)
    db.session.commit()

    return redirect(url_for('index'))

@app.route('/addpost', methods=['POST'])
def addpost():
    currencyCode = request.form['currencyCode']
    amount = request.form['amount']
    fromAccountId = request.form['fromAccountId']
    toAccountId = request.form['toAccountId']

    post = Transfer(currencyCode=currencyCode, amount=amount, fromAccountId=fromAccountId, toAccountId=toAccountId)

    db.session.add(post)
    db.session.commit()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)



