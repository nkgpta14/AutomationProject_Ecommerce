from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Flipkart.library import ConfigReader


def startBrowser():
    global driver
    if (ConfigReader.readConfigData('Details','Browser') == 'Chrome'):
        path = './drivers/chromedriver.exe'
        driver = Chrome(executable_path=path)
    elif (ConfigReader.readConfigData('Details','Browser') == 'Firefox'):
        path = './drivers/geckodriver.exe'
        driver = Firefox(executable_path=path)
    else:
        path = './drivers/chromedriver.exe'
        driver = Chrome(executable_path=path)
    driver.maximize_window()
    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    return driver
