# authour: Zachary Christian
# date: 20200419
import stockRequest, config, json, csv
from time import strftime
import os
from os import path

# I am going to have to call this function with a parameter
# for the stock ticker as well as one for the config key
def retrieveStockData(ticker, key):
    stockJson = json.loads(stockRequest.getQuote(ticker,key).text)
    
    currTime = strftime('%H%M%S')
    currDate = strftime('%Y%m%d')
    openPrice = stockJson['open']
    currPrice = stockJson['iexRealtimePrice']

    if openPrice == None:
        openPrice = stockJson['previousClose']
    fromOpen = openPrice - currPrice

    dataArray= [openPrice, currPrice, fromOpen, currTime, currDate]
    print(dataArray)
    return dataArray

# createFileForTicker makes a csv file with the column names
# open, current price, data
def createFileForTicker(ticker):
    with open(str(ticker).upper() + str('.csv'), 'w', newline='') as file:
        csv.writer(file).writerow(['Open', 'Current Price','From Open',  'Time', 'Date'])
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
#
def checkForStockFile(ticker, stockData):
    currDate = strftime('%Y%m%d')
    tickerFinal = str(ticker) + str(currDate)

    if path.exists(str(ticker) + str(".csv")):
        appendDataToFile(ticker, stockData)
    else:
        createFileForTicker(ticker)
        appendDataToFile(ticker, stockData)

    if path.exists(str(tickerFinal) + str('.csv')):
        appendDataToFile(tickerFinal, stockData)
    else:
        createFileForTicker(tickerFinal)
        appendDataToFile(tickerFinal, stockData)

# This function checks for a dir that is the name of
# the ticker we are tracking and if it is not created
# it creates the dir then switches to its path
# and then executes the checkForStockFile function
# inside

def checkForStockDir(ticker):
    currPath = os.getcwd()
    tmp = str('/') + str(ticker)
    # this is the final path for the stock ticker file
    tickerPath = currPath + tmp

    if path.exists(str(ticker)):
        os.chdir(tickerPath)
        checkForStockFile(ticker, retrieveStockData(ticker, config.key))
        os.chdir(currPath)
        # going to add checkForStockFile here
    else:
        os.mkdir(tickerPath.upper())
        os.chdir(tickerPath)
        checkForStockFile(ticker, retrieveStockData(ticker, config.key))
        os.chdir(currPath)
        # going to add checkForStockFile here







