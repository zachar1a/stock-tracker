# autor: Zachary Christian
# date: 2019/3/03

import os, time, datetime, requests, json
import stockInfo as si
import config,time
from datetime import datetime

def getQuote(ticker, key):
    getQuoteUrl = "https://cloud.iexapis.com/beta/stock/%(ticker)s/quote?token=%(key)s"%({'key':key, 'ticker':ticker})
    return requests.get(getQuoteUrl)
    
        
def retrieveDataFromResponse(responseFromAPI):
    return json.loads(responseFromAPI.text)

def sendToJSON():
    ticker = input("Stock ticker: ")
    stockData = retrieveDataFromResponse(getQuote(ticker, config.key))
    print(stockData['iexRealtimePrice'])
    print(datetime.now().strftime("%H%M%S"))
    



