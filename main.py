# author: Zachary Christian
# date: 20200419

import stockLog as sl
import time
from time import strftime

ticker = input("ticker: ")
currTime = strftime('%H')

# TODO 
'''
    check for the path of the ticker with with the date
    appended to it and then open a graph with the data from
    that file.
    If one is not available then use the checkForStockDir
    function to quickly make the dir and file to be used
    then open the graph with data

    In while loop I need to update graph with new data
'''
while int(strftime('%H')) >= 8:
    sl.checkForStockDir(ticker)
    time.sleep(2)
