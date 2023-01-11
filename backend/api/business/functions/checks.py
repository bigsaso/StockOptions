from business.screener.Screener import check_index, check_stock
from business.functions.gather_data import get_nasdaq100
from yahoo_fin.stock_info import tickers_sp500 as sp500

def check_nasdaq100():
    result = check_index(get_nasdaq100)
    return result

def check_sp500():
    result = check_index(sp500)
    return result

def check_individual_stock(ticker):
    result = check_stock(ticker)
    return result

if __name__ == '__main__':
    result = check_nasdaq100()
    print(result)