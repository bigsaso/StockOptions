from datetime import datetime as dt

def screener(company):
    time = dt.now().strftime('%Y/%m/%d')
    streak = ''
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
        if(today_upper_bb < today_upper_kc and today_lower_bb > today_lower_kc and today_price > today_ma and today_momentum > 0 and current_status!='Put'):
            current_status = 'Call'
            streak = '5 Days'
        elif(today_upper_bb < today_upper_kc and today_lower_bb > today_lower_kc and today_price < today_ma and today_momentum < 0 and current_status!='Call'):
            current_status = 'Put'
            streak = '5 Days'
        else:
            if day ==-5:
                streak = '4 Days'
            elif day ==-4:
                streak = '3 Days'
            elif day ==-3:
                streak = '2 Days'
            elif day ==-2:
                streak = '1 Day'
            break
    return ticker,current_status,streak,time