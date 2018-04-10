import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from selenium.webdriver.common.by import By

class NavigationPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _main_page = "//div[@id='_desktop_logo']/a[@href='http://localhost/prestashop/']" #byxpath
    _search_input = 's' #byName
    _clothes_page ='category-3' #byID


    def backToHomePage(self):
        self.elementClick(locator=self._main_page, locatorType="xpath")

    def goToClothesPage(self):
        self.elementClick(locator=self._clothes_page)

    def clearCartandGoToMainPage(self):
        self.backToHomePage()
        self.waitForElement(locator="cart-products-count",locatorType="class")
        self.elementClick(locator="cart-products-count",locatorType="class")
        self.waitForElement(locator="//a[@href='http://localhost/prestashop/koszyk?delete=1&id_product=30&id_product_attribute=150&token=41accb438c23197911beb3a379f403de']/i[.='delete']",
                            locatorType="xpath")
        trashcans = self.driver.find_elements(By.XPATH, "//section[@id='main']//ul[@class='cart-items']//a/i")
        for trashcan in trashcans:
            self.elementClick(element=trashcan)
        self.waitForElement(locator="no-items", locatorType="class")

    def goToContactPage(self):
        self.webScroll(direction="down")
        self.elementClick(locator="link-static-page-contact-2", locatorType="id")
        self.waitForElement(locator="contact-form", locatorType="class")