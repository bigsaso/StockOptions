from db import db

class OneDayModel(db.Model):
    __tablename__ = "onedaystreak"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5))