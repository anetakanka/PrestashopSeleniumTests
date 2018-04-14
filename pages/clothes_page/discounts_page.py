import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import logging
from base.basepage import BasePage
from pages.home_page.navigation import NavigationPage
from pages.home_page.login_page import LoginPage


class DiscountsPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)
        self.lp = LoginPage(driver)

    #Loctors
    _discount_info_clothes_page = "//div[@class='products row']//span[@class='discount-percentage discount-product']" #byXpath
    _panda_tshirt = "//div[@id='js-product-list']/div[@class='products row']//a[contains(text(),'T-shirt Panda')]" #byXpath
    _discount_info_element = "//div[@class='product-prices']//span[@class='discount discount-percentage']"
    _panda_tshirt_current_price = "//section[@id='main']//div[@class='product-prices']/div[2]//span[1]"
    _panda_tshirt_regular_price = "//div[@class='product-prices']//span[@class='regular-price']"

    def priceCheck(self, discountnum):
        currentPrice = self.driver.find_element(By.XPATH, self._panda_tshirt_current_price).get_attribute("content")
        currentPrice= currentPrice.replace(",", ".")
        regularPrice = self.driver.find_element(By.XPATH,self._panda_tshirt_regular_price).text
        regularPrice = regularPrice.replace("zł", "")
        regularPrice = regularPrice.replace(",",".")
        discount = float(regularPrice) * float(discountnum)
        if (float(regularPrice) - float(discount)) == float(currentPrice):
            return True
        return False

    def discountForLoggedInClientSuccessful(self, email, password, discountnum):
        self.lp.login(email, password)
        self.nav.goToClothesPage()
        self.waitForElement(locator=self._panda_tshirt, locatorType='xpath')
        self.elementClick(locator=self._panda_tshirt, locatorType='xpath')
        discountInfo = self.isElementPresent(locator=self._discount_info_element, locatorType='xpath')
        if discountInfo and self.priceCheck(discountnum):
            result = True
        else:
            result = False
        self.lp.logout()
        return result

    def discountForLoggedInClientFailed(self):
        self.nav.goToClothesPage()
        self.waitForElement(locator=self._panda_tshirt, locatorType='xpath')
        self.elementClick(locator=self._panda_tshirt, locatorType='xpath')
        result = self.isElementPresent(locator=self._discount_info_element, locatorType='xpath')
        return result

    def discountInfoOnClothesPageElements(self,email,password, elementNum):
        self.lp.login(email, password)
        self.nav.goToClothesPage()
        self.waitForElement(locator="//div[@id='js-product-list']/div[@class='products row']/article[1]",
                            locatorType='xpath')
        discountInfo = self.driver.find_elements(By.XPATH,self._discount_info_clothes_page)
        if len(discountInfo) == elementNum:
            result = True
        else:
            result = False
        self.lp.logout()
        return result





