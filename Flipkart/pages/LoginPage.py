from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from Flipkart.library import ConfigReader
from selenium.webdriver.common.keys import Keys


class LoginPageClass():

    def __init__(self,browser):
        global wait
        global driver
        driver = browser
        wait = WebDriverWait(driver, 10)

    def loginWindow(self):
        driver.find_element(By.XPATH,ConfigReader.fetchElement('Login','loginwindow_popup_XPATH')).click()


    def category(self,category):
        ctgry_srch_txtbx = wait.until(ec.element_to_be_clickable(
            (By.NAME, ConfigReader.fetchElement('Login', 'searchCategory_textbox_NAME'))))
        ctgry_srch_txtbx.send_keys(Keys.CONTROL,'a')
        ctgry_srch_txtbx.send_keys(category)
        ctgry_srch_txtbx.submit()


    def categoryCorrection(self,category):
        srch_bx_ctgry = driver.find_element(
            By.NAME, ConfigReader.fetchElement('Login', 'searchCategory_textbox_NAME')).get_property('value')
        while srch_bx_ctgry != category:
            LoginPageClass(driver).category(category)
            if srch_bx_ctgry.text == category:
                break
