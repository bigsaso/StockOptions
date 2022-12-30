from screener.Screener import check_index, check_stock
from functions.gather_data import get_nasdaq100
from yahoo_fin.stock_info import tickers_sp500 as sp500

def check_nasdaq100():
    stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours = check_index(get_nasdaq100)
    return stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours

def check_sp500():
    stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours = check_index(sp500)
    return stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours

def check_individual_stock(ticker):
    stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours = check_stock(ticker)
    return stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours

if __name__ == '__main__':
    stock_calls,stock_puts,stock_ones,stock_twos,stock_threes,stock_fours = check_nasdaq100()
    print(f'Calls ({len(stock_calls)}): {stock_calls}\nPuts ({len(stock_puts)}): {stock_puts}\n4-days Streak ({len(stock_fours)}): {stock_fours}\n3-days Streak ({len(stock_threes)}): {stock_threes}\n2-days Streak ({len(stock_twos)}): {stock_twos}\n1-day Streak ({len(stock_ones)}): {stock_ones}')