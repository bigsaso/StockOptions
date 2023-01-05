from flask import Blueprint
from functions.checks import check_nasdaq100, check_sp500

stock_routes = Blueprint('server_routes', __name__)

# Initialize temp memory -> Will transfer to DB
nasdaq100_calls,nasdaq100_puts,nasdaq100_ones,nasdaq100_twos,nasdaq100_threes,nasdaq100_fours = ([] for i in range(6))
sp500_calls,sp500_puts,sp500_ones,sp500_twos,sp500_threes,sp500_fours = ([] for i in range(6))

# API Endpoint to update NASDAQ100 Screener Results
@stock_routes.post('/checkNasdaq100')
def update_nasdaq100():
    global nasdaq100_calls
    global nasdaq100_puts
    global nasdaq100_ones
    global nasdaq100_twos
    global nasdaq100_threes
    global nasdaq100_fours
    nasdaq100_calls,nasdaq100_puts,nasdaq100_ones,nasdaq100_twos,nasdaq100_threes,nasdaq100_fours = ([] for i in range(6))
    nasdaq100_calls,nasdaq100_puts,nasdaq100_ones,nasdaq100_twos,nasdaq100_threes,nasdaq100_fours = check_nasdaq100()
    return 'PASS'

# API Endpoint to get NASDAQ100 Screener Results
@stock_routes.get('/getNasdaq100')
def get_nasdaq100_info():
    global nasdaq100_calls
    global nasdaq100_puts
    global nasdaq100_ones
    global nasdaq100_twos
    global nasdaq100_threes
    global nasdaq100_fours
    return {'Calls': nasdaq100_calls, 'Puts': nasdaq100_puts, 'OneDayStreak': nasdaq100_ones, 'TwoDaysStreak': nasdaq100_twos, 'ThreeDaysStreak': nasdaq100_threes, 'FourDaysStreak': nasdaq100_fours}

# API Endpoint to update S&P500 Screener Results
@stock_routes.post('/checkSp500')
def update_sp500():
    global sp500_calls
    global sp500_puts
    global sp500_ones
    global sp500_twos
    global sp500_threes
    global sp500_fours
    sp500_calls,sp500_puts,sp500_ones,sp500_twos,sp500_threes,sp500_fours = ([] for i in range(6))
    sp500_calls,sp500_puts,sp500_ones,sp500_twos,sp500_threes,sp500_fours = check_sp500()
    return 'PASS'

# API Endpoint to get S&P500 Screener Results
@stock_routes.get('/getSp500')
def get_sp500_info():
    global sp500_calls
    global sp500_puts
    global sp500_ones
    global sp500_twos
    global sp500_threes
    global sp500_fours
    return {'Calls': sp500_calls, 'Puts': sp500_puts, 'OneDayStreak': sp500_ones, 'TwoDaysStreak': sp500_twos, 'ThreeDaysStreak': sp500_threes, 'FourDaysStreak': sp500_fours}