import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import logging
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver


class productSearch(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #Locators

    _search_input = 's' #byName
    _search_input_submit = '//div[@id="search_widget"]//button[@type="submit"]' #byXpath
    _first_element_in_list = '//div[@class="products row"]/article[1]' #byXpath
    _elements_list = '//div[@class="products row"]/article' #byXpath
    _elements_list_ank = '//div[@class="products row"]/article//div[@class="product-description"]//a' #byXpath
    _repeat_search_button = '//section[@id="content"]/div[@id="search_widget"]' #byXpath

    def searchProductsByText(self, text):
        self.sendKeys(text, locator=self._search_input, locatorType='name')
        self.elementClick(locator=self._search_input_submit, locatorType='xpath')

    def searchSuccesfulByNum(self, numindatabase):
        # Compares the number of products after search on the website to the number of products in the database
        self.waitForElement(locator=self._first_element_in_list, locatorType='xpath', pollFrequency=1)
        product_list = self.driver.find_elements(By.XPATH, self._elements_list)
        num = len(product_list)
        if str(num) == numindatabase:
            result = True
        else:
            result = False
        return result

    def searchFailed(self):
        self.waitForElement(locator=self._repeat_search_button, locatorType='xpath')
        result = self.isElementPresent(locator=self._repeat_search_button, locatorType='xpath')
        return result

    def searchSuccessfulByText(self, text):
        product_list = self.driver.find_elements(By.XPATH, self._elements_list_ank)
        if product_list is not None:
            for el in product_list:
                if text not in el.text.lower():
                    return False
            return True
        return False









