from gather_data import gather_data

def screener(company):
    calls = ''
    puts = ''
    fail = ''
    days_to_check = [-1,-2,-3,-4,-5]
    current_status = ''
    for day in days_to_check:
        today = company.iloc[day]
        ticker = today['ticker']
        today_price = today['close']
        today_upper_kc = today['upper_KC']
        today_lower_kc = today['lower_KC']
        today_upper_bb = today['bollinger_up']
        today_lower_bb = today['bollinger_down']
        today_ma = today['MA']
        today_momentum = today['momentum']
        if(today_upper_bb < today_upper_kc and today_lower_bb > today_lower_kc and today_price > today_ma and today_momentum > 0 and current_status!='put'):
            #print(f'{ticker} - PASS CALLS')
            calls = ticker
            current_status = 'call'
        elif(today_upper_bb < today_upper_kc and today_lower_bb > today_lower_kc and today_price < today_ma and today_momentum < 0 and current_status!='call'):
            #print(f'{ticker} - PASS PUTS')
            puts = ticker
            current_status = 'put'
        else:
            if day !=-1:
                #print(f'{ticker} - FAIL')
                calls = ''
                puts = ''
                fail = f'{ticker} failed {current_status} {(day)*(-1)-1} day(s) ago'
            break
    return calls,puts,fail

## TRIAL SCREENER ##
# company = gather_data('AMD.csv')
# screener(company)

