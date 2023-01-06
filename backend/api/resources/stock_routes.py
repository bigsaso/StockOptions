from flask import Blueprint
from functions.checks import check_nasdaq100, check_sp500

stock_routes = Blueprint('server_routes', __name__)

# Initialize temp memory -> Will transfer to DB
nasdaq100_result = []
sp500_result = []

# API Endpoint to update NASDAQ100 Screener Results
@stock_routes.post('/checkNasdaq100')
def update_nasdaq100():
    global nasdaq100_result
    nasdaq100_result.clear()
    nasdaq100_result = check_nasdaq100()
    return 'PASS'

# API Endpoint to get NASDAQ100 Screener Results
@stock_routes.get('/getNasdaq100')
def get_nasdaq100_info():
    global nasdaq100_result
    return nasdaq100_result

# # API Endpoint to update S&P500 Screener Results
# @stock_routes.post('/checkSp500')
# def update_sp500():
#     global sp500_result
#     sp500_result = []
#     sp500_result = check_sp500()
#     return 'PASS'

# # API Endpoint to get S&P500 Screener Results
# @stock_routes.get('/getSp500')
# def get_sp500_info():
#     global sp500_result
#     return sp500_result