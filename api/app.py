from flask import Flask
from flask_cors import CORS
import os

from resources.stock_routes import stock_routes
from db import db
import models

def create_app(db_url=None):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()
    app.register_blueprint(stock_routes)
    CORS(app, resources={r"/*": {"origins": "*"}})

    return app

# if __name__ == '__main__':
#     app.run(debug=True)