from src.data.gather_data import gather_data

def screener(company):
    today = company.iloc[-1]
    ticker = today['ticker']
    today_price = today['close']
    today_upper_kc = today['upper_KC']
    today_lower_kc = today['lower_KC']
    today_upper_bb = today['bollinger_up']
    today_lower_bb = today['bollinger_down']
    today_ma = today['MA']
    today_momentum = today['momentum']
    if(today_upper_bb < today_upper_kc and today_lower_bb > today_lower_kc and today_price > today_ma and today_momentum > 0):
        print(f'{ticker} - PASS')
    else:
        #print(f'{ticker} - FAIL')
        pass

## TRIAL SCREENER ##
# company = gather_data('AMD.csv')
# screener(company)

