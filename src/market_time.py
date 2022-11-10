import datetime
from yahoo_fin.stock_info import get_premarket_price,get_postmarket_price

def is_premarket(current):
    start = datetime.time(4,0,0)
    end = datetime.time(9,30,0)
    return start<=current<=end

def is_postmarket(current):
    start = datetime.time(16,0,0)
    end = datetime.time(20,0,0)
    return start<=current<=end

def get_pre_post_market(ticker,current_hour):
    if is_premarket(current_hour):
        data = get_premarket_price(ticker)
    elif is_postmarket(current_hour):
        data = get_postmarket_price(ticker)
    #company = gather_data(data)
    print(data)

if __name__ == '__main__':
    current_hour = datetime.datetime.now().time()
    get_pre_post_market('AAPL',current_hour)