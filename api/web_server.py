from flask import Flask
from flask_cors import CORS
from stock_routes import stock_routes

app = Flask(__name__)
app.register_blueprint(stock_routes)
CORS(app, resources={r"/*": {"origins": "*"}})

if __name__ == '__main__':
    app.run(debug=True)