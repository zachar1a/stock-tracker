import config
import stockLog as sl
from time import strftime

ticker = input("ticker: ")

currTime = strftime('%H')
print(currTime)

sl.checkForStockDir(ticker)
