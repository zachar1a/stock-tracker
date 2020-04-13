import numpy as np
import matplotlib.pyplot as plt
import json

#this is for the open price
def getOpenPrice(): 
    open_price=[]

    with open('csvjson.json') as jf:
        myArr=json.loads(jf.read())

    for i in range(len(myArr)):
        open_price.append(myArr[i]['Open'])

    return open_price

#this is for the date
def getDate():
    date=[]

    with open('csvjson.json') as jf:
        myArr=json.loads(jf.read())
    # here we have to strip the hyphens off of the date
    # to get it in a pure number form
    for i in range(len(myArr)):
        s=myArr[i]['Date'].replace('-','')
        date.append(s)

    return date

#this is to get the size of the array
def getListSize():
    with open('csvjson.json') as jf:
        myArr=json.loads(jf.read())
    return len(myArr)


#this is the main plotting function
def main():

    open_price=getOpenPrice()
    date=getDate()

    myArrSize=getListSize()

    x_avg=[date[0],date[myArrSize-1]]
    y_avg=[open_price[0],open_price[myArrSize-1]]

    plt.plot(date,open_price)
    plt.plot(x_avg,y_avg)

    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    print("plotting")

    plt.show()

main()
