import datetime
from dateutil.relativedelta import relativedelta
from yahoo_fin.stock_info import get_data,tickers_dow,tickers_nasdaq,tickers_sp500
from yahoo_fin.options import get_calls,get_puts,get_expiration_dates

from gather_data import gather_data
from screener_algorithm import screener

today = datetime.date.today()
last_year = (datetime.datetime.now()-relativedelta(years=1))

# Check an index
dow = tickers_sp500()
dow_hist = {}
for ticker in dow:
    #dow_hist[ticker] = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
    data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
    company = gather_data(data)
    screener(company)

# Check individual stock
# data = get_data('MO', start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
# company = gather_data(data)
# screener(company)

# Experimenting with Calls/Puts display
# exp_dates = get_expiration_dates('MO')
# for date in exp_dates[:5]:
#     print(get_calls('MO'),date)