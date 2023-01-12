from flask import Flask
from flask_cors import CORS

from resources.stock_routes import stock_routes
from resources.auth import auth

app = Flask(__name__)
app.register_blueprint(stock_routes)
app.register_blueprint(auth)
CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(debug=True)