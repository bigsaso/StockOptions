from flask import Blueprint
from business.functions.checks import check_nasdaq100

stock_routes = Blueprint('stock_routes', __name__)

# Initialize temp memory -> Will transfer to DB
nasdaq100_result = []

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