import datetime as dt
from dateutil.relativedelta import relativedelta
from yahoo_fin.stock_info import get_data, tickers_sp500 as sp500

from functions.gather_data import gather_data
from screener.screener_algorithm import screener

today = dt.date.today()
last_year = (dt.datetime.now()-relativedelta(years=1))

calls = []
puts = []
fails = []
ones = []
twos = []
threes = []
fours = []

# Check an index
def check_index(function):
    index = function()
    index_hist = {}
    for ticker in index:
        data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
        company = gather_data(data)
        company_calls,company_puts,company_ones,company_twos,company_threes,company_fours = screener(company)
        if company_calls!='':
            calls.append(company_calls)
        if company_puts!='':
            puts.append(company_puts)
        if company_ones!='':
            ones.append(company_ones)
        if company_twos!='':
            twos.append(company_twos)
        if company_threes!='':
            threes.append(company_threes)
        if company_fours!='':
            fours.append(company_fours)
    return calls,puts,ones,twos,threes,fours


# Check individual stock
def check_stock(ticker):
    data = get_data(ticker, start_date = last_year, end_date = today, index_as_date = True, interval = '1d')
    company = gather_data(data)
    company_calls,company_puts,company_ones,company_twos,company_threes,company_fours = screener(company)
    if company_calls!='':
        calls.append(company_calls)
    if company_puts!='':
        puts.append(company_puts)
    if company_ones!='':
        ones.append(company_ones)
    if company_twos!='':
        twos.append(company_twos)
    if company_threes!='':
        threes.append(company_threes)
    if company_fours!='':
        fours.append(company_fours)
    return calls,puts,ones,twos,threes,fours

# Check custom stock
def check_custom_stock(csv):
    company = gather_data(csv)
    company_calls,company_puts,company_ones,company_twos,company_threes,company_fours = screener(company)
    if company_calls!='':
        calls.append(company_calls)
    if company_puts!='':
        puts.append(company_puts)
    if company_ones!='':
        ones.append(company_ones)
    if company_twos!='':
        twos.append(company_twos)
    if company_threes!='':
        threes.append(company_threes)
    if company_fours!='':
        fours.append(company_fours)
    return calls,puts,ones,twos,threes,fours