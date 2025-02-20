# from . import db
# from sqlalchemy.sql import func

# class Artwork(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(150), unique=True)
#     product_type = db.Column(db.String(150))
#     art_style = db.Column(db.String(150))
 
# class Commission(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150))
#     details = db.Column(db.String(150))
#     request_date = db.Column(db.DateTime(timezone=True), default=func.now())


# ------------------------------------------------------------


# from . import db
# from sqlalchemy.sql import func

# class Commission(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     email = db.Column(db.String(150), nullable=False)
#     request = db.Column(db.String(500), nullable=False)
#     questions = db.Column(db.String(300), nullable=True)
#     deadline = db.Column(db.Date, nullable=False)
#     request_date = db.Column(db.DateTime(timezone=True), default=func.now())

