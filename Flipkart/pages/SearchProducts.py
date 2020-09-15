from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from Flipkart.library import ConfigReader
import random, sys


class ProductSelection():

    def __init__(self, browser):
        global wait
        global driver
        driver = browser
        wait = WebDriverWait(driver,10)

    def selectBrand(self,brand):
        search_brand_txtbx = wait.until(ec.element_to_be_clickable(
                    (By.XPATH,ConfigReader.fetchElement('SearchProduct','searchbrand_textbox_XPATH'))))
        driver.execute_script("arguments[0].click();", search_brand_txtbx)
        search_brand_txtbx.send_keys(Keys.CONTROL, 'a')
        search_brand_txtbx.send_keys(brand)

        brand_chckbx = wait.until(ec.element_to_be_clickable(
                    (By.XPATH,ConfigReader.fetchElement('SearchProduct','brand_selection_XPATH'))))
        driver.execute_script("arguments[0].click();", brand_chckbx)


    def selectionOfProduct(self,category,brand):

        url = driver.current_url
        if (not brand in url):
            ProductSelection(driver).clearFilter(category)
            ProductSelection(driver).selectBrand(brand)
            print(brand + ' brand is selected')
        else:
            pass
        products = wait.until(ec.visibility_of_all_elements_located(
            (By.XPATH,ConfigReader.fetchElement('SearchProduct', 'product_selection_XPATH'))))
        driver.execute_script("arguments[0].click();", products[0])

    def shoeSizeSelection(self):

        shoe_sizelist = wait.until(
            ec.presence_of_all_elements_located(
                (By.XPATH, ConfigReader.fetchElement('SearchProduct', 'shoe_size_list_XPATH'))))
        random.choice(shoe_sizelist).click()

    def productAddition(self,category):

        all_windows = driver.window_handles
        for win in all_windows:
            driver.switch_to.window(win)
            URL_window_handle = driver.current_url
            if category in URL_window_handle:
                pass
            else:
                if category == 'Shoes' :
                    ProductSelection(driver).shoeSizeSelection()
                ProductSelection(driver).additionToCart()

    def additionToCart(self):

        try:
            wait.until(ec.element_to_be_clickable(
                (By.XPATH, ConfigReader.fetchElement('SearchProduct', 'add_To_cart_XPATH')))).click()
            wait.until(ec.url_to_be(ConfigReader.fetchElement('SearchProduct', 'cart_matching_URL')))
            driver.close()
        except:
            print('Product is not available currently, we will notify once it is available')
            driver.close()

    def clearFilter(self,category):

        all_windows = driver.window_handles
        for win in all_windows :
            driver.switch_to.window(win)
            URL_window_handle = driver.current_url
            if category in URL_window_handle :
                clear_filter = wait.until(ec.element_to_be_clickable(
                    (By.XPATH, ConfigReader.fetchElement('SearchProduct', 'filter_clear_textbox_XPATH'))))
                driver.execute_script("arguments[0].click();", clear_filter)
                driver.refresh()
                url_filter = driver.current_url
                if (('facets.brand') in url_filter) :
                    driver.execute_script("arguments[0].click();", clear_filter)
            else :
                pass


    def cartAddition(self,category,brand):
        try:
            all_windows = driver.window_handles
            for win in all_windows :
                driver.switch_to.window(win)
                URL_window_handle = driver.current_url
                if category in URL_window_handle :
                    pass
                else :
                    url_product = driver.current_url
                    brand_lower = brand.lower()
                    if brand_lower in url_product:
                        try:
                            ProductSelection(driver).productAddition(category)
                        except:
                            print('productAddition - if block', sys.exc_info()[0], "occurred.")
                    else:
                        try:
                            driver.close()
                            ProductSelection(driver).clearFilter(category)
                            ProductSelection(driver).selectBrand(brand)
                            url = driver.current_url
                            if (not brand in url) :
                                ProductSelection(driver).clearFilter(category)
                                ProductSelection(driver).selectBrand(brand)
                                print(brand + ' brand is selected')
                            else :
                                pass
                            ProductSelection(driver).selectionOfProduct(category,brand)
                            ProductSelection(driver).productAddition(category)
                        except:
                            print('productAddition - else block', sys.exc_info()[0], "occurred.")
        except:
            print('cartAddition', sys.exc_info()[0], "occurred.")





