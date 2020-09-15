from Flipkart.pages.Flipkart_EndToEnd import MainClass
from Flipkart.data.Constant import Config
from Flipkart.baseFiles import InitiateDriver
import sys


def test_Flipkart():
    try:
        driver = InitiateDriver.startBrowser()
        MainClass(driver).closeLoginWindow()
        for category in Config().categories:
            MainClass(driver).searchCategory(category)
            if category == 'Mobiles':
                for brand in Config().brand_list1:
                    MainClass(driver).brandSelection(brand)
                    MainClass(driver).productSelection(category,brand)
                    MainClass(driver).addToCart(category,brand)
                    MainClass(driver).filterClear(category)
            else:
                for brand in Config().brand_list2:
                    MainClass(driver).brandSelection(brand)
                    MainClass(driver).productSelection(category,brand)
                    MainClass(driver).addToCart(category,brand)
                    MainClass(driver).filterClear(category)
        MainClass(driver).checkOut()
        MainClass(driver).cartClear()
    except:
        print('Test end-to-end flow', sys.exc_info()[0], "occurred.")
        pass
