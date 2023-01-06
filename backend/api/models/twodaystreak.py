from db import db

class TwoDaysModel(db.Model):
    __tablename__ = "twodaystreak"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5))