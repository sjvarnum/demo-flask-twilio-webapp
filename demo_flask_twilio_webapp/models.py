from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db

# Admin user accounts - require auth
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)

# Contact list
class Contact(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    create_date = db.Column(db.DateTime, default=datetime.utcnow)