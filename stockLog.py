import stockRequest, config, json

'''
    I am going to try and log all of this info inside of
    a csv file and then use that file to graph the stock
    daily
'''

# items in stockInfo

# symbol
# companyName
# high
# low
# latestPrice
# latestSource
# calculationPrice
# stockOpen
# openTime
# close

def stockLogging():
    stockJson = json.loads(stockRequest.getQuote('aapl', config.key).text)

    
