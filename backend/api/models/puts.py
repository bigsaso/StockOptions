from db import db

class PutsModel(db.Model):
    __tablename__ = "puts"
    id = db.Column(db.Integer, primary_key=True)
    ticker = db.Column(db.String(5))