from Flipkart.pages.Flipkart_EndToEnd import MainClass
from Flipkart.baseFiles.InitiateDriver import startBrowser
from Flipkart.data import Data
import sys


def test_Flipkart():
    try:
        driver = startBrowser()
        MainClass(driver).closeLoginWindow()
        rows = Data.getRowCount()
        columns = Data.getColumnCount()
        #We are fetching data from excel -
        #1st row is header and data is getting started from 2nd row.
        for row_category in range(2,rows+1):
            MainClass(driver).searchCategory(Data.readData(row_category, 1))
            for row_brand in range(2,columns+1):
                MainClass(driver).brandSelection(Data.readData(row_category, row_brand))
                MainClass(driver).productSelection(Data.readData(row_category, 1), Data.readData(row_category, row_brand))
                MainClass(driver).addToCart(Data.readData(row_category, 1), Data.readData(row_category, row_brand))
                MainClass(driver).filterClear(Data.readData(row_category, 1))
        MainClass(driver).checkOut()
        MainClass(driver).cartClear()
    except:
        print('Test Flipkart(Data Driven) - EndToEnd', sys.exc_info()[0], "occurred.")
        pass
