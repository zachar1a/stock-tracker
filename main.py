# autor: Zachary Christian
# date: 2019/3/03

import os, time, datetime, requests, json
import stockInfo as si
import config
def getQuote(ticker, key):
    getQuoteUrl = "https://cloud.iexapis.com/beta/stock/%(ticker)s/quote?token=%(key)s"%({'key':key, 'ticker':ticker})
    getQuteRequest = requests.get(getQuoteUrl)
    return getQuteRequest
# Storing request into json var myQuote
def getQuoteData():
    quote = getQuote(ticker,key)
    myQuote = json.loads(quote.text)
    return myQuote
# Using this to put the values to default keys
def quoteInfo():
    myQuote = getQuoteData()
    for key, value in si.stock.stockStats.items():
        if key in myQuote:
            si.stock.stockStats[key] = myQuote[key]
        else:
            pass

# This is where i am logging the info to file   # These vars have to be kept out of the main function so they can be global variables
def initLog(myQuote):
    currentDT = datetime.datetime.now()
    month = currentDT.strftime("%b")
    numDay = currentDT.strftime("%d")
    mOpen = myQuote['open']
    mClose = myQuote['latestPrice']
    # if either myQuote['open'] or myQuote['latestPrice'] are none i set 
    # var newPrice to none
    if mOpen is None:
        mOpen = myQuote['previousClose']
        newPrice =float(myQuote['latestPrice']) - float(mOpen)
    else:
        newPrice = float(myQuote['latestPrice']) - float(myQuote['open'])
    # This checks if a file with the stock ticker exists
    if os.path.exists("./%(file)s.txt"%({"file": myQuote['symbol']})):
        stockFile = open("%(symbol)s.txt"%({"symbol": myQuote['symbol']}), "a")
        stockFile.write("date " + str(myQuote['latestTime']) + "newest price: " + str(newPrice) + "\n")
        print("date " + str(myQuote['latestTime']) + " newest price: " + str(myQuote['close']))
        stockFile.close()
    # If stock ticker file does not exist this creates one
    else:
        stockFile = open("%(symbol)s.txt"%({"symbol": myQuote['symbol']}), "w")
        stockFile.write(myQuote['companyName'] + " "  + "close: " + str(myQuote['close']) + " open: " + str(mOpen) + "\n")
        print(myQuote['companyName'] + " "  + "close: " + str(myQuote['close']) + " open: " + str(mOpen))
        stockFile.close()
    logFile = str(myQuote['symbol'] + month + str(numDay))
    # Checks if log file exists
    # Log file name consists of ticker month and date so i can have records or activity
    if os.path.exists("./%(logFile)s.txt"%({"logFile": logFile})):
        log = open("%(logFile)s.txt"%({"logFile": logFile}), "a")
    # This logs the ticker-openPrice-latestPrice-newPrice
        log.write(myQuote['symbol'] + " open " + str(mOpen) + " latest price " + str(myQuote['latestPrice']) + "  mvmnt " + str(newPrice) + "\n")
        print(myQuote['symbol'] + " open " + str(mOpen) + " latest price " + str(myQuote['latestPrice']) + "  mvmnt " + str(newPrice))
        log.close()
    # If log file does not exist I make one
    else:
        log = open("%(logFile)s.txt"%({"logFile": logFile}), "w")
    # This logs the ticker-openPrice-latestPrice-newPrice
        log.write(myQuote['symbol'] + " open " + str(myQuote['open']) + " latest price " + str(myQuote['latestPrice']) + "  mvmnt " + str(newPrice) + "\n")
        print(myQuote['symbol'] + " open " + str(myQuote['open']) + " latest price " + str(myQuote['latestPrice']) + "  mvmnt " + str(newPrice))
        log.close()
        
def quoteLoop():
    # getQuote gets the request
    # initLog logs important data from request
    getQuote(ticker, key)
    myQuote = getQuoteData()
    initLog(myQuote)

def quoteUpdater():
    currentDT = datetime.datetime.now()
    day = currentDT.strftime("%a")
    hour = currentDT.strftime("%H")
    # This checks if current day is not saturday or sunday
    invalidDays = ["Sun", "Sat"]
    for days in invalidDays:
    # If day is not saturday or sunday then I check if the time is
    # Between 8 and 5 when the markets are open
        if day == days or int(hour) < 8 or int(hour) > 16: 
            print("Markets are closed")
            break
        else:
    # This is a while loop that checks the hour and while it is less than
    # 17 (5pm) then it will continue
    # It has a sleeper function that puts it to rest for a minute
    # Then loops over the getQuote and initLog functions
            while int(hour) < 17:
                quoteLoop()
                time.sleep(60)
            break
    # These vars have to be kept out of the main function so they can be global variables
ticker = input("What stock would you like to keep track of: ")
key = config.key
def main():
    quoteInfo()
    quoteUpdater()
main()
