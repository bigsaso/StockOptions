import requests
from requests.exceptions import ConnectionError
from lxml import etree
from io import StringIO

def get_sentiment(tree):
    refs = tree.xpath("/html/body/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[1]/a")
    # links = [etree.tostring(link) for link in refs]
    sentiment = [link.text for link in refs]
    return [l for l in sentiment]

def get_longterm(tree):
    refs = tree.xpath("/html/body/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/p[2]")
    # links = [etree.tostring(link) for link in refs]
    sentiment = [link.text for link in refs]
    return [l for l in sentiment]

def get_warnings(tree):
    refs = tree.xpath("/html/body/main/div/div[2]/div[2]/div/div[2]/div/div[2]/div[1]/div/div[2]/p[3]")
    # links = [etree.tostring(link) for link in refs]
    sentiment = [link.text for link in refs]
    return [l for l in sentiment]

def analyze_sentiment(ticker):
    URL = f"https://www.barchart.com/stocks/quotes/{ticker}/overview"
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0'}
    parser = etree.HTMLParser()
    try:
        page = requests.get(URL,headers=headers)
        html = page.content.decode("utf-8")
        tree = etree.parse(StringIO(html), parser=parser)
        sentiment = get_sentiment(tree)
        longterm = get_longterm(tree)
        warnings = get_warnings(tree)
        return sentiment[0],longterm[0],warnings[0]
    except ConnectionError:
        return "Connection Error","Connection Error","Connection Error"