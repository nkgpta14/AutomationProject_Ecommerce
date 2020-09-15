from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException,ElementNotInteractableException,StaleElementReferenceException,ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
import random
import sys
import time

category = ['Mobiles','Shoes']
brand_list = ['Apple', 'Samsung']
brand_list1 = ['Arrow', 'ADIDAS']


def loginWindow():
    try:
        browser.find_element(By.XPATH, "//div[@id='container']/following-sibling::div/div/div/button").click()
    except TimeoutException:
        print('Login window', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def searchCategory(category):
    try:
        search = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.NAME,'q')))
        searchClear()
        search.send_keys(category)
        search.submit()
    except TimeoutException as e:
        print('Search Category', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def searchClear():
    try:
        time.sleep(0.5)
        search = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.NAME,'q')))
        search.click()
        search.send_keys(Keys.CONTROL + 'a')
        search.send_keys(Keys.DELETE)
    except TimeoutException:
        print('Clear Main Search', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def searchBrand(y):
    try:
        time.sleep(1)
        brands = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
            (By.XPATH, "//input[@type='text' and @class='_3vKPvR']")))
        browser.execute_script("arguments[0].click();", brands)
        brands.clear()
        brands.send_keys(y)
        search_brands = WebDriverWait(browser,10).until(ec.presence_of_all_elements_located(
            (By.XPATH,
             "//*[@class='_1GEhLw' and contains(text(),'" + y + "')]")))
        browser.execute_script("arguments[0].click();", search_brands[0])
    except (TimeoutException,ElementNotInteractableException):
        print('Search Brand', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def productSelection(k):
    try:
        products = WebDriverWait(browser,10).until(ec.presence_of_all_elements_located(
                (By.XPATH,
                 "//div[contains(text(),'" + k + "')]/parent::div/parent::div")))
        time.sleep(1)
        products[1].click()
    except (ElementClickInterceptedException,TimeoutException):
        print('Product Selection', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def addToCart(x):
    try:
        browser.switch_to.window(browser.window_handles[1])
        if x == 'Shoes':
            try:
                sizelist = WebDriverWait(browser,10).until(
                    ec.presence_of_all_elements_located((By.XPATH, '//a[@class="_1TJldG _2I_hq9 _2UBURg"]')))
                random.choice(sizelist).click()
            except TimeoutException:
                print('Shoe Size selection', sys.exc_info()[0], "occurred.")
        try:
            cart = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
                    (By.XPATH, "//button[@class='_2AkmmA _2Npkh4 _2MWPVK']")))
            cart.click()
            time.sleep(1)
            browser.close()
        except:
            print('Product is not available currently, we will notify once it is available')
            browser.close()
    except ElementClickInterceptedException:
        print('Adding to Cart', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def filterClear():
    try:
        browser.switch_to.window(browser.window_handles[0])
        filter_clear = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='_1oXuet']")))
        browser.execute_script("arguments[0].click();", filter_clear)
    except TimeoutException:
        print('Filter Clear', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def checkOut():
    try:
        checkout = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
                (By.XPATH,'//span[contains(text(),"Cart")]')))
        checkout.click()
    except TimeoutException:
        print('Checkout', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def cartClear():
    try:
        cart_list = WebDriverWait(browser,10).until(ec.presence_of_all_elements_located(
                        (By.XPATH, '//a[@class="_325-ji _3ROAwx"]')))
        print(cart_list)
        for item in cart_list:
            remove = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
                (By.XPATH, "//div[@class='gdUKd9' and contains(text(),'Remove')]")))
            remove.click()
            removeConfirmation()
            print(str(item) + ' has been removed')
            time.sleep(0.30)
        browser.close()
    except TimeoutException:
        print('Cart Clear', sys.exc_info()[0], "occurred.")
        browser.close()
        exit()

def removeConfirmation():
    try:
        remove_confirmation = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@class='gdUKd9 _3Z4XMp _2nQDKB']")))
        remove_confirmation.click()
        time.sleep(0.25)
    except:
        print('Remove Confirmation', sys.exc_info()[0], "occurred.")
        exit()

try:
    i = 1
    while i <= 3:
        browser = webdriver.Chrome(executable_path='C:\Program Files\chromedriver')
        browser.maximize_window()
        browser.get('https://www.flipkart.com/')

        loginWindow()
        for x in category:
            searchCategory(x)
            if x == 'Mobiles':
                for y in brand_list:
                    searchBrand(y)
                    productSelection(y)
                    addToCart(x)
                    filterClear()
            else:
                for z in brand_list1:
                    searchBrand(z)
                    productSelection(z)
                    addToCart(x)
                    filterClear()
            searchClear()
        checkOut()
        cartClear()
        print('iteration Number ' + str(i))
        i += 1
except StaleElementReferenceException:
    pass
