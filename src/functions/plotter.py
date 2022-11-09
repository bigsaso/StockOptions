# import pandas as pd
# import numpy as np
import matplotlib.pyplot as plt
from yahoo_fin.stock_info import get_data
import datetime
from dateutil.relativedelta import relativedelta

# from bollinger_bands import get_BB, get_SMA
from src.data.gather_data import gather_data
# from keltner_channel import get_ATR, get_EMA, get_KC
# from momentum import get_momentum

## TRIAL GRAPH ##

# From custom CSV
# df = pd.read_csv('AMD.csv')
# print(df.head())
# closing_prices = df['Close']
# high_prices = df['High']
# low_prices = df['Low']
# SMA = get_SMA(closing_prices,20)
# EMA = get_EMA(closing_prices,20)
# ATR = get_ATR(high_prices,low_prices,closing_prices,14)
# upper_KC,lower_KC = get_KC(EMA,1.5,ATR)
# bollinger_up,bollinger_down = get_BB(closing_prices,20,14,1.5)
# MA = get_SMA(closing_prices,14)
# momentum = get_momentum(closing_prices,14)

# From function import
today = datetime.date.today()
last_year = (datetime.datetime.now()-relativedelta(years=1))
ticker = 'EA'
data = get_data(ticker=ticker, start_date = last_year, end_date = None, index_as_date = True, interval = '1d')
df = gather_data(data)
plt.title(ticker + ' Graph')
plt.xlabel('Days')
plt.ylabel('Closing Prices')
plt.plot(df['close'], label='Closing Prices')
plt.plot(df['bollinger_up'], label='Bollinger Up', c='green')
plt.plot(df['bollinger_down'], label='Bollinger Down', c='red')
plt.plot(df['upper_KC'], label='Upper Keltner Channel', c='black')
plt.plot(df['lower_KC'], label='Lower Keltner Channel', c='black')
plt.plot(df['MA'], label='MA 14-Days', c='purple')
plt.plot(df['momentum'], label='14-day Momentum', c='blue')
plt.legend()
plt.show()