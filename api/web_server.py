from flask import Flask
from stock_routes import stock_routes

app = Flask(__name__)
app.register_blueprint(stock_routes)

if __name__ == '__main__':
    app.run(debug=True)