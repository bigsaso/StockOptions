import datetime
from dateutil.relativedelta import relativedelta
from yahoo_fin.stock_info import get_data,tickers_dow as dow,tickers_nasdaq as nasdaq,tickers_sp500 as sp500
from yahoo_fin.options import get_calls,get_puts,get_expiration_dates

from src.data.gather_data import gather_data
from src.functions.screener_algorithm import screener

today = datetime.date.today()
last_year = (datetime.datetime.now()-relativedelta(years=1))

# Check an index
def check_index(function):
    index = function()
    index_hist = {}
    for ticker in index:
        #dow_hist[ticker] = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
        data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
        company = gather_data(data)
        screener(company)

# Check individual stock
def check_stock(ticker):
    data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
    company = gather_data(data)
    screener(company)

def check_custom_stock(csv):
    company = gather_data(csv)
    screener(company)

# Experimenting with Calls/Puts display
# exp_dates = get_expiration_dates('MO')
# for date in exp_dates[:5]:
#     print(get_calls('MO'),date)

if __name__ == '__main__':
    check_index(sp500)