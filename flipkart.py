from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

category = ['Mobiles','Shoes']
brand_list = ['Apple', 'Samsung', 'Motorola']
brand_list1 = ['Nike', 'ADIDAS', 'Sparx']



def loginWindow():
    try:
        browser.find_element(By.XPATH, "//div[@id='container']/following-sibling::div/div/div/button").click()
    except TimeoutException:
        print('Login Page is not loaded successfully')
        browser.close()

def searchCategory(category):
    try:
        search = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.NAME,'q')))
        searchClear()
        search.send_keys(category)
        search.submit()
    except TimeoutException:
        print('Search Box is not loaded')
        browser.close()

def searchClear():
    try:
        time.sleep(1)
        search = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.NAME,'q')))
        search.click()
    #    act = ActionChains(browser)
    #    act.key_down(Keys.CONTROL).send_keys_to_element(search,'a').perform()
    #    act.send_keys_to_element(search,Keys.DELETE).perform()
        search.send_keys(Keys.CONTROL + 'a')
        search.send_keys(Keys.DELETE)
    except TimeoutException:
        print('SearchClear Box is not loaded')
        browser.close()

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
    except TimeoutException:
        print('Search Brand is not loaded')
        browser.close()
        exit()
    except ElementClickInterceptedException:
        print('Click is intercepted')
        browser.close()
        exit()

def product(k,count):
    try:
        time.sleep(2)
        product = WebDriverWait(browser,10).until(ec.presence_of_all_elements_located(
                (By.XPATH,
                 "//div[contains(text(),'" + k + "')]/parent::div/parent::div")))
        product[count].click()
    except ElementClickInterceptedException:
        print('Product is not loaded properly')
        browser.quit()
        exit()

def cart(x,size):
    try:
        browser.switch_to.window(browser.window_handles[1])
        if x == 'Shoes':
            try:
                sizelist = WebDriverWait(browser,10).until(
                    ec.presence_of_all_elements_located((By.XPATH, '//a[@class="_1TJldG _2I_hq9 _2UBURg"]')))
                if len(sizelist) > size:
                    sizelist[size].click()
                else:
                    sizelist[0].click()
            except TimeoutException:
                print('No such element is available')
        try:
            cart = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
                    (By.XPATH, "//button[@class='_2AkmmA _2Npkh4 _2MWPVK']")))
            cart.click()
            time.sleep(1)
            browser.close()
        except TimeoutException:
            print('Product is not available currently, we will notify once it is available')
            browser.close()
    except ElementClickInterceptedException:
        print('Cart is not loaded properly')
        browser.close()
        exit()

def filterClear():
    try:
        browser.switch_to.window(browser.window_handles[0])
        filter_clear = WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH, "//div[@class='_1oXuet']")))
        #filter_clear.click()
        time.sleep(2)
        browser.execute_script("arguments[0].click();", filter_clear)
    except TimeoutException:
        print('Session is Timed Out - Filter has not been cleared')
        browser.close()
        exit()

def checkOut():
    try:
        checkout = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
                (By.XPATH,'//span[contains(text(),"Cart")]')))
        checkout.click()
    except TimeoutException:
        print('List not found')
        browser.close()
        exit()

def cartClear():
    try:
        cart_list = WebDriverWait(browser,10).until(ec.presence_of_all_elements_located(
                        (By.XPATH, '//a[@class="_325-ji _3ROAwx"]')))
        #print(cart_list)
        for item in cart_list:
            print(item)
            remove = WebDriverWait(browser,10).until(ec.element_to_be_clickable(
                (By.XPATH, "//div[@class='gdUKd9' and contains(text(),'Remove')]")))
            remove.click()
            removeConfirmation()
    except TimeoutException:
        print('Cart has not been loaded properly')
        browser.close()
        exit()

def removeConfirmation():
    try:
        remove_confirmation = WebDriverWait(browser, 10).until(ec.element_to_be_clickable(
            (By.XPATH, "//div[@class='gdUKd9 _3Z4XMp _2nQDKB']")))
        remove_confirmation.click()
        time.sleep(1)
    except TimeoutException:
        print('No Remove button found')
        browser.close()
        exit()

try:
    i = 1
    count = 1
    while i <= 10:
        browser = webdriver.Chrome(executable_path='C:\Program Files\chromedriver')
        browser.maximize_window()
        browser.get('https://www.flipkart.com/')
        browser.implicitly_wait(10)

        loginWindow()
        for x in category:
            searchCategory(x)
            if x == 'Mobiles':
                size = ''
                for y in brand_list:
                    searchBrand(y)
                    product(y,count)
                    cart(x,size)
                    filterClear()
            else:
                size = 0
                for z in brand_list1:
                    searchBrand(z)
                    product(z,count)
                    cart(x,size)
                    size += 1
                    filterClear()
            searchClear()
        checkOut()
        time.sleep(1)
        cartClear()
        browser.quit()
        print('Number of Iteration ' + str(i))
        i += 1
        count += 1
except StaleElementReferenceException:
    pass
