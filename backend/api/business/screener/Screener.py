import datetime as dt
from dateutil.relativedelta import relativedelta
from yahoo_fin.stock_info import get_data, tickers_sp500 as sp500

from business.functions.gather_data import gather_data
from business.screener.screener_algorithm import screener
from business.indicators.sentiment import analyze_sentiment

# today = dt.date.today()
last_year = (dt.datetime.now()-relativedelta(years=1))

results = []

# Check an index
def check_index(function):
    index = function()
    for ticker in index:
        data = get_data(ticker, start_date = last_year, index_as_date = True, interval = '1d')#, end_date = today
        company = gather_data(data)
        company_ticker,company_status,company_streak,scan_date = screener(company)
        if company_status:
            sentiment,lt,warnings = analyze_sentiment(company_ticker)
            # rsi = round(company.iloc[-1]['RSI'],2)
            results.append({"Ticker": company_ticker, "Status": company_status, "Streak": company_streak, "Scan Date": scan_date, "ST Sentiment": sentiment, "LT Analysis": lt, "Warnings": warnings})#, "RSI": rsi
    return results


# Check individual stock
def check_stock(ticker):
    data = get_data(ticker, start_date = last_year, index_as_date = True, interval = '1d')#, end_date = today
    company = gather_data(data)
    company_ticker,company_status,company_streak,scan_date = screener(company)
    if company_status:
        sentiment,lt,warnings = analyze_sentiment(company_ticker)
        results.append({"Ticker": company_ticker, "Status": company_status, "Streak": company_streak, "Scan Date": scan_date, "ST Sentiment": sentiment, "LT Analysis": lt, "Warnings": warnings})
    return results

# Check custom stock
def check_custom_stock(csv):
    company = gather_data(csv)
    company_ticker,company_status,company_streak,scan_date = screener(company)
    if company_status:
        sentiment,lt,warnings = analyze_sentiment(company_ticker)
        results.append({"Ticker": company_ticker, "Status": company_status, "Streak": company_streak, "Scan Date": scan_date, "ST Sentiment": sentiment, "LT Analysis": lt, "Warnings": warnings})
    return results