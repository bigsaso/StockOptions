from db import db

class ThreeDaysModel(db.Model):
    __tablename__ = "threedaystreak"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5))