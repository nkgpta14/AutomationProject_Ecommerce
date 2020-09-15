#from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from Helper import *

category = ['Mobiles','Shoes']
brand_list = ['Moto','Samsung','Apple']
brand_list1 = ['Arrow','Nike','Sparx']

try:
    i = 1
    productCount = 1
    while i <= 3:
        browser = webdriver.Chrome(executable_path='C:\Program Files\chromedriver')
        browser.maximize_window()
        browser.get('https://www.flipkart.com/')

        loginWindow(browser)
        for categoryName in category:
            try:
                searchCategory(categoryName,browser)
                if categoryName == 'Mobiles':
                    size = ''
                    for y in brand_list:
                        searchBrand(y,browser)
                        product1 = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located(
                            (By.XPATH,
                                "//div[contains(text(),'" + y + "')]/parent::div/parent::div")))
                        #print(len(product1))
                        if len(product1) > i:
                            selectProduct(y,productCount,browser)
                            addToCart(categoryName, size,browser)
                            filterClear(browser)
                        else:
                            print('Product is not available to select')
                            continue
                else:
                    size = 0
                    for productBrandname in brand_list1:
                        #print('brand Names are ' + str(brand_list1))
                        #print('Selected brand in loop is ' + z)
                        #try:
                        searchBrand(productBrandname,browser)
                        # try:
                        product1 = WebDriverWait(browser, 10).until(ec.presence_of_all_elements_located(
                            (By.XPATH,
                             "//div[contains(text(),'" + productBrandname + "')]/parent::div/parent::div")))
                        #print(len(product1))
                        if len(product1) > 1:
                            selectProduct(productBrandname,productCount,browser)
                            addToCart(categoryName,size,browser)
                            size += 1
                            filterClear(browser)
                        else:
                            print('Product is not available to select')
                            filterClear(browser)
                            continue
                        #except TimeoutException:
                        #    print('Page is not loaded for multiple brands search')
            except TimeoutException:
                print('Something is not right - Element not found')
                browser.close()
            searchClear(browser)
        checkOut(browser)
        time.sleep(1)
        removeProduct(browser)
        print('Number of Iteration ' + str(i))
        browser.quit()
        i += 1
        productCount += 1
except StaleElementReferenceException:
    pass

sys.exc_info()[0], "occurred."