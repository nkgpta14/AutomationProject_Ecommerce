from Flipkart.pages.LoginPage import LoginPageClass
from Flipkart.pages.SearchProducts import ProductSelection
from Flipkart.pages.Cart import CartClass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Flipkart.library import ConfigReader
from selenium.common.exceptions import NoSuchElementException
import sys


class MainClass():

    def __init__(self,browser):
        global wait
        global driver
        driver = browser

        wait = WebDriverWait(driver,10)


    def closeLoginWindow(self):
        try:
            LoginPageClass(driver).loginWindow()
        except NoSuchElementException:
            pass
        except:
            print('Login window', sys.exc_info()[0], "occurred.")
            LoginPageClass(driver).loginWindow()


    def searchCategory(self,category):
        try:
            LoginPageClass(driver).category(category)
            LoginPageClass(driver).categoryCorrection(category)
        except:
            print(sys.exc_info()[0], "occurred in 'Search Category'.")
            LoginPageClass(driver).category(category)
            LoginPageClass(driver).categoryCorrection(category)


    def brandSelection(self,brand):
        try:
           ProductSelection(driver).selectBrand(brand)
        except:
            print('Brand Selection', sys.exc_info()[0], "occurred.")
            ProductSelection(driver).selectBrand(brand)


    def productSelection(self,category,brand):
        try:
            ProductSelection(driver).selectionOfProduct(category,brand)
        except :
            print('Product Selection', sys.exc_info()[0], "occurred.")
            ProductSelection(driver).selectionOfProduct(category,brand)


    def addToCart(self,category,brand):
        try:
            ProductSelection(driver).cartAddition(category,brand)
        except :
            print('Add to Cart', sys.exc_info()[0], "occurred.")
            ProductSelection(driver).cartAddition(category,brand)


    def filterClear(self,category):
        try:
            ProductSelection(driver).clearFilter(category)
        except :
            print('Filter Clear', sys.exc_info()[0], "occurred.")
            ProductSelection(driver).clearFilter(category)

    def checkOut(self):
        try:
            CartClass(driver).cartCheckOut()
        except:
            print('Checkout', sys.exc_info()[0], "occurred.")
            CartClass(driver).cartCheckOut()


    def cartClear(self):
        try:
            CartClass(driver).removeProduct()
            wait.until(ec.presence_of_element_located(
                (By.XPATH, ConfigReader.fetchElement('Cart', 'empty_cart_XPATH'))))
        except:
            print('Cart Clear', sys.exc_info()[0], "occurred.")
            CartClass(driver).removeProduct()
        finally:
            assert wait.until(ec.presence_of_element_located(
                    (By.XPATH, ConfigReader.fetchElement('Cart','empty_cart_XPATH'))))
            driver.close()
