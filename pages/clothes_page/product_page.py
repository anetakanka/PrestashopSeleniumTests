import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home_page.navigation import NavigationPage

class ProductPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _product_title = "h1" #byclass
    _product_description = "product-description-short-30" #byId
    _size_S = '//div[@id="search_filters"]/section[2]/ul/li[1]//span[@class="custom-checkbox"]'
    _zoom_in_img = "material-icons zoom-in" #byClass
    _enlarge_img = "//div[@role='document']//figure/img" #byxpath width = 800
    _img = "//div[@class='images-container']/div[1]/img" #byxpath
    _panda_tshirt = "//div[@id='js-product-list']/div[@class='products row']//a[contains(text(),'T-shirt Panda')]"  # byXpath
    _product_availability = "product-availability" #byID
    _add_to_cart = "//form[@id='add-to-cart-or-refresh']//button[@type='submit']"

    def goToProductPage(self):
        self.nav.goToClothesPage()
        self.waitForElement(locator=self._panda_tshirt, locatorType="xpath")
        self.elementClick(locator=self._panda_tshirt, locatorType="xpath")
        self.waitForElement(locator=self._product_title, locatorType="class")

    def productTitle(self,title):
        self.goToProductPage()
        product = self.getElement(locator=self._product_title, locatorType="class")
        productTitle = product.text.lower()
        if title == productTitle:
            result = True
        else:
            result = False
        return result

    def productDescription(self,description):
        self.goToProductPage()
        productDescription = self.getElement(locator=self._product_description).text
        if description == productDescription:
            result = True
        else:
            result = False
        return result

    def imgDisplayed(self):
        self.goToProductPage()
        result = self.isElementDisplayed(locator=self._img, locatorType="xpath")
        return result

    def imgEnlarge(self):
        self.goToProductPage()
        self.elementClick(locator=self._zoom_in_img, locatorType="class")
        self.waitForElement(locator=self._enlarge_img, locatorType="xpath")
        img = self.getElement(locator=self._enlarge_img, locatorType="xpath")
        width = img.get_attribute("width")
        if width == "800":
            result = True
        else:
            result = False
        return result

    def sizeNotAvailable(self):
        self.goToProductPage()
        self.elementClick(locator=self._size_S, locatorType="xpath")
        self.waitForElement(locator=self._product_availability)
        availability = self.isElementDisplayed(locator=self._product_availability)
        addToCart = self.getElement(locator=self._add_to_cart, locatorType="xpath")
        addToCartStatus = addToCart.is_enabled()
        if (addToCartStatus == False) and (availability == True):
            result = True
        else:
            result = False
        return result





