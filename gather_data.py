import pandas

from bollinger_bands import get_BB, get_SMA
from keltner_channel import get_ATR, get_EMA, get_KC
from momentum import get_momentum

def gather_data(data):
    if not isinstance(data,pandas.core.frame.DataFrame):
        df = pandas.read_csv(data)
    else:
        df = data
    closing_prices = df['close']
    high_prices = df['high']
    low_prices = df['low']
    df['SMA'] = get_SMA(closing_prices,20)
    df['EMA'] = get_EMA(closing_prices,20)
    df['ATR'] = get_ATR(high_prices,low_prices,closing_prices,14)
    df['upper_KC'],df['lower_KC'] = get_KC(df['EMA'],1.5,df['ATR'])
    df['bollinger_up'],df['bollinger_down'] = get_BB(closing_prices,20,14,1.5)
    df['MA'] = get_SMA(closing_prices,14)
    df['momentum'] = get_momentum(closing_prices,14)
    return df

# ## TRIAL DATA ##
# company = gather_data('AMD.csv')
# print(company.tail())