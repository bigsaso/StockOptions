import datetime as dt
from yahoo_fin.stock_info import get_premarket_price,get_postmarket_price

def is_premarket(current):
    start = dt.time(4,0,0)
    end = dt.time(9,30,0)
    return start<=current<=end

def is_postmarket(current):
    start = dt.time(16,0,0)
    end = dt.time(20,0,0)
    return start<=current<=end

def get_pre_post_market(ticker,current_hour):
    if is_premarket(current_hour):
        data = f'{ticker} Premarket: {get_premarket_price(ticker)}'
    elif is_postmarket(current_hour):
        data = f'{ticker} Postmarket: {get_postmarket_price(ticker)}'
    else:
        data = f'{ticker} Not pre/post market'
    print(data)

if __name__ == '__main__':
    current_hour = dt.datetime.now().time()
    get_pre_post_market('CL',current_hour)