import os, time, datetime, requests, json, config
import stockInfo as si

key = config.key
ticker = "AAPL"
getQuoteUrl = "https://cloud.iexapis.com/beta/stock/%(ticker)s/quote?token=%(key)s"%({'key':key, 'ticker':ticker})

quoteJson = json.loads(requests.get(getQuoteUrl).text)

print(quoteJson)


