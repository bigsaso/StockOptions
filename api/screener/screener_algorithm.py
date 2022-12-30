def screener(company):
    calls = ''
    puts = ''
    one_day_streak = ''
    two_days_streak = ''
    three_days_streak = ''
    four_days_streak = ''
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
            calls = ticker
            current_status = 'call'
        elif(today_upper_bb < today_upper_kc and today_lower_bb > today_lower_kc and today_price < today_ma and today_momentum < 0 and current_status!='call'):
            puts = ticker
            current_status = 'put'
        else:
            if day ==-5:
                calls = ''
                puts = ''
                four_days_streak = ticker + ' - ' + current_status
            elif day ==-4:
                calls = ''
                puts = ''
                three_days_streak = ticker + ' - ' + current_status
            elif day ==-3:
                calls = ''
                puts = ''
                two_days_streak = ticker + ' - ' + current_status
            elif day ==-2:
                calls = ''
                puts = ''
                one_day_streak = ticker + ' - ' + current_status
            break
    return calls,puts,one_day_streak,two_days_streak,three_days_streak,four_days_streak