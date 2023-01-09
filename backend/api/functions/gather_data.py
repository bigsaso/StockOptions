import pandas as pd
import requests

from indicators.bollinger_bands import get_BB, get_SMA
from indicators.keltner_channel import get_ATR, get_EMA, get_KC
from indicators.momentum import get_momentum
from indicators.rsi import get_rsi

def gather_data(data):
    if not isinstance(data,pd.core.frame.DataFrame):
        df = pd.read_csv(data)
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
    df['RSI'] = get_rsi(closing_prices)
    return df

def get_nasdaq100():
    tickers = []
    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"}
    res = requests.get("https://api.nasdaq.com/api/quote/list-type/nasdaq100", headers=headers)
    main_data = res.json()['data']['data']['rows']
    for company in main_data:
        tickers.append(company['symbol'])
    return tickers