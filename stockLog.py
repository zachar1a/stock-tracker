import stockRequest, config, json, csv
from time import strftime
from os import path

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

# I am going to have to call this function with a parameter
# for the stock ticker as well as one for the config key
def retrieveStockData(ticker, key):
    stockJson = json.loads(stockRequest.getQuote(ticker,key).text)
    currTime = strftime('%H%M%S')
    dataArray= [stockJson['open'], stockJson['latestPrice'], stockJson['latestPrice']-stockJson['open'],currTime]
    return dataArray

# createFileForTicker makes a csv file with the column names
# open, current price, data
def createFileForTicker(ticker):
    with open(str(ticker).upper() + str('.csv'), 'w', newline='') as file:
        csv.writer(file).writerow(['Open', 'Current Price', 'From Open', 'Time'])
        file.close()

# appendDataToFile appends the important data to the csv file
def appendDataToFile(ticker, stockData):
    with open(str(ticker) + str('.csv'), 'a', newline='') as file:
        worker = csv.writer(file)
        worker.writerow(stockData)
        file.close()

# this is going to check for a file with the title of the stock ticker
# for instance, the Apple inc. file would be, AAPL
#
# this function is going to have multiple parts
# 1) to check if the file is created,
#
# 2) create the file if not existed:
#    a) need to make cell names for data:
#       open, current price, time of price
#
# 3) if the file is created, then append data to file
def checkForStockFile(ticker, stockData):
    if path.exists(str(ticker) + str(".csv")):
        appendDataToFile(ticker, stockData)
    else:
        createFileForTicker(ticker)
        appendDataToFile(ticker, stockData)

ticker = input("what ticker do you want to track: ")
checkForStockFile(ticker, retrieveStockData(ticker, config.key))








