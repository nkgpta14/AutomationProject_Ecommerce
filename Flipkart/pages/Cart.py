from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Flipkart.library import ConfigReader


class CartClass():

    def __init__(self,browser):
        global wait
        global driver
        driver = browser
        wait = WebDriverWait(driver,10)

    def cartCheckOut(self):
        wait.until(ec.element_to_be_clickable(
            (By.XPATH,ConfigReader.fetchElement('Cart','checkout_webelement_XPATH')))).click()

    def removeProduct(self):
        cart_prd_list = wait.until(ec.visibility_of_all_elements_located(
            (By.XPATH, ConfigReader.fetchElement('Cart', 'cart_elements_XPATH'))))

        for items in cart_prd_list :
            rmv_prd_btn = wait.until(ec.element_to_be_clickable(
                (By.XPATH, ConfigReader.fetchElement('Cart', 'remove_button_XPATH'))))
            driver.execute_script("arguments[0].click();", rmv_prd_btn)

            rmv_prd_cnfrm_popup_btn = wait.until(ec.element_to_be_clickable(
                (By.XPATH, ConfigReader.fetchElement('Cart','remove_confirmation_button_XPATH'))))
            driver.execute_script("arguments[0].click();", rmv_prd_cnfrm_popup_btn)
            driver.refresh()




