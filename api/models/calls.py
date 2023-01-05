from db import db

class CallsModel(db.Model):
    __tablename__ = "calls"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5))