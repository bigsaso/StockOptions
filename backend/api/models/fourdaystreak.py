from db import db

class FourDaysModel(db.Model):
    __tablename__ = "fourdaystreak"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5))