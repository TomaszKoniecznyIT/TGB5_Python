import os
from dotenv import load_dotenv
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://bzbghcqv:JiV57VJyJcUd5SPsSZIpYmPrqZiZX_l8@flora.db.elephantsql.com/bzbghcqv'
print(os.getenv('SQLALCHEMY_DATABASE_URI'))
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password_hash = db.Column(db.String(360), nullable=False)

    @property
    def password(self):
        raise AttributeError('Password is not a readable attribute!')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verif_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self) -> str:
        return f'User email: {self.email}'


class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    shop_code = db.Column(db.String(15), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Shop: {self.name}'


class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.DateTime, nullable=False)
    target = db.Column(db.Float,nullable=False)
    id_shop = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Target: {self.target} Month: {self.month}'


class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.DateTime, nullable=False)
    total = db.Column(db.Float, nullable=False)
    id_shop = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Day: {self.day} total: {self.total}'

@app.route('/users/signup', methods=['POST'])
def add_user():
    data = request.json()
