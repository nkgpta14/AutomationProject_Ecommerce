import time
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import sys

browser = ''

def loginWindow(browser):
    try:
        WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@id='container']/following-sibling::div/div/div/button"))).click()
    except NoSuchElementException:
        print('loginwindow','NoSuchElementException','Login Page is not loaded successfully')
        browser.close()
        exit()
    except TimeoutException:
        print('loginwindow','TimeoutException',"Login window didn't load properly")
        browser.close()

def searchCategory(category,browser):
    try:
        search = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.NAME, 'q')))
        searchClear(browser)
        search.send_keys(category)
        search.submit()
    except TimeoutException:
        print('searchCategory','TimeoutException','Search Box is not loaded')
        browser.close()
        exit()

def searchClear(browser):
    try:
        #time.sleep(1)
        search = WebDriverWait(browser, 10).until(ec.element_to_be_clickable((By.NAME, 'q')))
        search.click()
        search.send_keys(Keys.CONTROL + 'a')
        search.send_keys(Keys.DELETE)
    except TimeoutException:
        print('searchClear','TimeoutException','SearchClear Box is not loaded')
        browser.close()
        exit()


def searchBrand(productBrandName, browser):
    try:
        time.sleep(1)
        brands = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//input[@type='text' and @class='_3vKPvR']")))
        browser.execute_script("arguments[0].click();", brands)
        print("Search brand","Element is visible? " + str(brands.is_displayed()))
        # brands.clear()
        # time.sleep(1)
        # brands.click()
        brands.send_keys(Keys.CONTROL + 'a')
        brands.send_keys(Keys.DELETE)
        time.sleep(2)
        print("Search brand","Before XPATH " ,productBrandName )

        brands.send_keys(productBrandName)

        search_brands = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH,
             "//*[@class='_1GEhLw' and contains(text(),'" + productBrandName + "')]")))
        print("Search brand","After XPATH " , productBrandName)

        browser.execute_script("arguments[0].click();", search_brands[0])
    except NoSuchElementException:
        print('searchBrand','NoSuchElementException','Element is not found to select')
        browser.close()
        exit()
    except TimeoutException:
        print('searchBrand','TimeoutException','Search Brand is not loaded')
        browser.close()
        exit()
    except ElementClickInterceptedException:
        print('searchBrand','ElementClickInterceptedException','Click is intercepted')
        browser.close()
        exit()


def selectProduct(brandName,productCount,browser):
    try:
        time.sleep(2)
        productList = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH,
             "//div[contains(text(),'" + brandName + "')]/parent::div/parent::div")))
        #print(str(len(productList)) + ' is total number of products ')
        #browser.execute_script("arguments[0].click();", productList[productCount])


        productList[productCount].click()
        print('selectProduct', brandName)

    except ElementClickInterceptedException:
        print('selectProduct','ElementClickInterceptedException','Product is not loaded properly')
        browser.quit()
        exit()
    except TimeoutException:
        print('selectProduct','TimeoutException','Products are not loaded to select')
        browser.close()
        exit()


def addToCart(category, size, browser):
    try:
        browser.switch_to.window(browser.window_handles[1])
        #if category == 'Shoes':
        try:
            sizeList = WebDriverWait(browser, 10).until(
                ec.presence_of_all_elements_located((By.XPATH, '//a[@class="_1TJldG _2I_hq9 _2UBURg"]')))
            if len(sizeList) > size:
                sizeList[size].click()
            else:
                sizeList[0].click()
        except TimeoutException:
            print('addToCart','TimeoutException','No such element is available')
            print(sys.exc_info()[0], "occurred.")
        try:
            cart = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
                (By.XPATH, "//button[@class='_2AkmmA _2Npkh4 _2MWPVK']")))
            cart.click()
            #browser.execute_script("arguments[0].click();", cart)
            time.sleep(1)
            browser.close()
        except TimeoutException:
            print('addToCart','TimeoutException','Product is not available currently, we will notify once it is available')
            browser.close()
    except ElementClickInterceptedException:
        print('AddToCart','ElementClickInterceptedException','ElementClickInterceptedException')
        browser.close()
        exit()


def filterClear(browser):
    try:
        browser.switch_to.window(browser.window_handles[0])
        filter_clear = WebDriverWait(browser, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//div[@class='_1oXuet']")))
        # filter_clear.click()
        time.sleep(2)
        browser.execute_script("arguments[0].click();", filter_clear)
    except TimeoutException:
        print('filterClear','TimeoutException','Session is Timed Out - Filter has not been cleared')
        browser.close()
        exit()


def checkOut(browser):
    try:
        checkout = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
            (By.XPATH, '//span[contains(text(),"Cart")]')))
        checkout.click()
    except TimeoutException:
        print('checkOut','TimeoutException','List not found')
        browser.close()
        exit()


def removeProduct(browser):
    try:

        print('removeProduct', 'start')

        cart_list = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located(
            (By.XPATH, '//a[@class="_325-ji _3ROAwx"]')))
        print('removeproduct','end')
        # print(cart_list)
        for item in cart_list:
            print(item)
            remove = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
                (By.XPATH, "//div[@class='gdUKd9' and contains(text(),'Remove')]")))
            remove.click()
            removeConfirmationPopup(browser)
    except TimeoutException:
        print('removeProduct','TimeoutException','Cart has not been loaded properly')
        browser.close()
        exit()


def removeConfirmationPopup(browser):
    try:
        remove_confirmation = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@class='gdUKd9 _3Z4XMp _2nQDKB']")))
        remove_confirmation.click()
        time.sleep(1)
    except TimeoutException:
        print('removeConfirmationPopup','TimeoutException','No Remove button found')
        browser.close()
        exit()
