def get_rsi(closing_prices,days=14,ema = True):
    close_delta = closing_prices.diff()
    # Make up two series: one for lower closes and one for higher closes
    up = close_delta.clip(lower=0)
    down = -1*close_delta.clip(upper=0)
    if ema==True:
        # Use exponential moving average
        ma_up = up.ewm(com = days - 1, adjust=True, min_periods = days).mean()
        ma_down = down.ewm(com = days - 1, adjust=True, min_periods = days).mean()
    else:
        # Use simple moving average
        ma_up = up.rolling(days).mean()
        ma_down = down.rolling(days).mean()
    rs = ma_up / ma_down
    rsi = 100 - (100/(1 + rs))
    return rsi