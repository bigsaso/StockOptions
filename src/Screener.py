import datetime
from dateutil.relativedelta import relativedelta
from yahoo_fin.stock_info import get_data,tickers_dow as dow,tickers_nasdaq as nasdaq,tickers_sp500 as sp500
from yahoo_fin.options import get_calls,get_puts,get_expiration_dates

from gather_data import gather_data
from screener_algorithm import screener

today = datetime.date.today()
last_year = (datetime.datetime.now()-relativedelta(years=1))

calls = []
puts = []
fails = []

# Check an index
def check_index(function):
    index = function()
    index_hist = {}
    for ticker in index:
        #dow_hist[ticker] = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
        data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
        company = gather_data(data)
        company_calls,company_puts,company_fails = screener(company)
        if company_calls!='':
            calls.append(company_calls)
        if company_puts!='':
            puts.append(company_puts)
        if company_fails!='':
            fails.append(company_fails)
    return calls,puts,fails


# Check individual stock
def check_stock(ticker):
    data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
    company = gather_data(data)
    company_calls,company_puts,company_fails = screener(company)
    if company_calls!='':
            calls.append(company_calls)
    if company_puts!='':
        puts.append(company_puts)
    if company_fails!='':
        fails.append(company_fails)
    return calls,puts,fails

# Check custom stock
def check_custom_stock(csv):
    company = gather_data(csv)
    company_calls,company_puts,company_fails = screener(company)
    if company_calls!='':
            calls.append(company_calls)
    if company_puts!='':
        puts.append(company_puts)
    if company_fails!='':
        fails.append(company_fails)
    return calls,puts,fails

# Experimenting with Calls/Puts display
# exp_dates = get_expiration_dates('MO')
# for date in exp_dates[:5]:
#     print(get_calls('MO'),date)

if __name__ == '__main__':
    stock_calls,stock_puts,stock_fails = check_index(sp500)
    #stock_calls,stock_puts,stock_fails = check_stock('AXP')
    print(f'calls ({len(stock_calls)}): {stock_calls}\nputs ({len(stock_puts)}): {stock_puts}\nfails ({len(stock_fails)}): {stock_fails}')