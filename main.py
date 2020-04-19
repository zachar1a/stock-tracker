import stockLog, config
from time import strftime

ticker = input("ticker: ")

currTime = strftime('%H')
print(currTime)

stockLog.checkForStockFile(ticker, stockLog.retrieveStockData(ticker, config.key))

print(stockLog.retrieveStockData(ticker, config.key))
