# config/settings.py

import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.environ.get('mysql+pymysql://root:lasisa23$U@127.0.0.1:3306/money_transf') or 'mysql+pymysql://root:lasisa23$U@127.0.0.1:3306/money_transf'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
