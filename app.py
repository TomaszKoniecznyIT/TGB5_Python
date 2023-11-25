import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(360), nullable=False)

    def __repr__(self) -> str:
        return f'User email: {self.email}'
    
class Shop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    shop_code = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120),unique=True, nullable=False)
    password = db.Column(db.String(360), nullable=False)
    id_shop = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Shop: {self.name}'
    
class Target(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.DataTime, nullable=False)
    target = db.Column(db.Float,nullable=False)
    id_shop = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Target: {self.target} Month: {self.month}'
    
class Sale(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.DataTime, nullable=False)
    total = db.Column(db.Float, nullable=False)
    id_shop = db.Column(db.Integer, db.ForeignKey('shop.id'), nullable=False)

    def __repr__(self) -> str:
        return f'Day: {self.day} total: {self.total}'