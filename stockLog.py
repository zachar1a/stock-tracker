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
    dataArray= [stockJson['open'], stockJson['latestPrice'], stockJson['latestPrice']-stockJson['open'],currTime, currDate]
    return dataArray

# createFileForTicker makes a csv file with the column names
# open, current price, data
def createFileForTicker(ticker):
    with open(str(ticker).upper() + str('.csv'), 'w', newline='') as file:
        csv.writer(file).writerow(['Open', 'Current Price', 'From Open', 'Time', 'Date'])
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

# TODO @ZACHARY
# I am going to change the function to instead of adding
# only a file I am going to add a dir with the ticker name
# and then a file with the ticker and the date
# e.g TSLA would be TSLA20190419.csv
# and then I would have a main TSLA file that would have
# all of the data that I have tracked for the TSLA ticker 

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



def checkForStockDir(ticker):
    currPath = os.getcwd()
    tmp = str('/') + str(ticker)
    # this is the final path for the stock ticker file
    tickerPath = currPath + tmp

    if path.exists(str(ticker)):
        os.chdir(tickerPath)
        checkForStockFile(ticker, retrieveStockData(ticker, config.key))
        # going to add checkForStockFile here
    else:
        os.mkdir(tickerPath.upper())
        os.chdir(tickerPath)
        checkForStockFile(ticker, retrieveStockData(ticker, config.key))
        # going to add checkForStockFile here







