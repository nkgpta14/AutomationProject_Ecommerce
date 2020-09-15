from select import select
from selenium.webdriver.common.by import By

import pytest
from selenium.webdriver import Chrome



def test_valid_registration():
    driver = Chrome(executable_path='C:\Program Files\chromedriver')
    driver.get("http://www.theTestingworld.com/testing")
    driver.maximize_window()

#@pytest.mark.skipif(reason="dont want")
def test_invalid_registration_details():
        driver = Chrome(executable_path='C:\Program Files\chromedriver')
        driver.get("http://www.theTestingworld.com/testing")
        driver.maximize_window()
        obj = select(driver.find_element(By.LINK_TEXT,'Login'))
        obj.click()
        assert driver.current_url == "https://www.thetesting.com/index.php?option=com_users&view=login&Itemid=587"

def test_login():
    driver = Chrome(executable_path='C:\Program Files\chromedriver')
    driver.maximize_window()
    driver.get("http://www.thetestingworld.com/testing")