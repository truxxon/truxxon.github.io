from . import db
from sqlalchemy.sql import func
 
class Commission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), nullable=False)
    request = db.Column(db.String(500), nullable=False)
    questions = db.Column(db.String(300), nullable=True)
    deadline = db.Column(db.Date, nullable=False)
    request_date = db.Column(db.DateTime(timezone=True), default=func.now())

class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    style = db.Column(db.String(150), nullable=False)
    product_type = db.Column(db.String(150), nullable=False)
    artwork = db.Column(db.LargeBinary, nullable=False) 

class Bob(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    style = db.Column(db.String(150), nullable=False)
    product_type = db.Column(db.String(150), nullable=False)
    artwork = db.Column(db.LargeBinary, nullable=False) 

