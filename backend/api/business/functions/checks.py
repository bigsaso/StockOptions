from business.screener.Screener import check_index, check_stock
from business.functions.gather_data import get_nasdaq100

def check_nasdaq100():
    result = check_index(get_nasdaq100)
    return result

def check_individual_stock(ticker):
    result = check_stock(ticker)
    return result

if __name__ == '__main__':
    result = check_nasdaq100()
    print(result)