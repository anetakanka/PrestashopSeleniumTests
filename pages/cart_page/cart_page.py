import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import logging
from base.basepage import BasePage
from pages.home_page.navigation import NavigationPage
from pages.home_page.login_page import LoginPage
import time


class CartPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)
        self.lp = LoginPage(self.driver)

    #Loctors
    _cart = "_desktop_cart" #byID
    _add_to_cart = "//form[@id='add-to-cart-or-refresh']//button[@type='submit']"
    _panda_tshirt = "//div[@id='js-product-list']/div[@class='products row']//a[contains(text(),'T-shirt Panda')]"  # byXpath
    _bluzka_Fiona = "//div[@class='products row']//a[contains(text(),'Bluzka Fiona')]"
    _select_size = "group[1]" #byName
    _size_M = "//select[@name='group[1]']/option[@title='M']"
    _color = "group[2]" #byName
    _quantity = "quantity_wanted" #byID
    _go_to_fulfill_the_order_button = "//div[@class='modal-content']//a" #byxpath
    _continue_shopping_button = "//button[contains(text(),'Kontynuuj zakupy')]" #byxpath
    _num_of_products_in_cart = "//div[@id='cart-subtotal-products']/span[1]"
    _first_product_trashcan = "//ul[@class='cart-items']//a[@href='http://localhost/prestashop/koszyk?delete=1&id_product=30&id_product_attribute=150&token=41accb438c23197911beb3a379f403de']/i[.='delete']"
    _products_in_cart = "//div[@class='card cart-container']//ul[@class='cart-items']/li"
    _touchspin_down = "//div[@class='card cart-container']//li[1]/div[@class='product-line-grid']//span[@class='input-group-btn-vertical']/button[2]"

    def getProductToCartPanda(self, quantity):
        self.nav.goToClothesPage()
        self.waitForElement(locator="//div[@id='js-product-list']/div[@class='products row']/article[1]",
                            locatorType='xpath')
        self.elementClick(locator=self._panda_tshirt, locatorType='xpath')
        self.waitForElement(locator=self._size_M, locatorType="xpath")
        self.elementClick(locator=self._select_size, locatorType="name")
        self.elementClick(locator=self._size_M, locatorType="xpath")
        self.elementClick(locator=self._color, locatorType="name")
        self.clearField(locator=self._quantity)
        self.sendKeys(quantity, locator=self._quantity)
        time.sleep(2)
        self.elementClick(locator=self._add_to_cart, locatorType="xpath")
        self.waitForElement(locator="cart-content", locatorType="class")

    def getProductToCartFiona(self,quantity):
        self.nav.goToClothesPage()
        self.waitForElement(locator=self._bluzka_Fiona, locatorType='xpath')
        self.elementClick(locator=self._bluzka_Fiona, locatorType='xpath')
        self.waitForElement(locator=self._add_to_cart, locatorType="xpath")
        self.elementClick(locator=self._select_size, locatorType="name")
        self.elementClick(locator=self._size_M, locatorType="xpath")
        self.elementClick(locator=self._color, locatorType="name")
        self.clearField(locator=self._quantity)
        self.sendKeys(quantity, locator=self._quantity)
        self.elementClick(locator=self._add_to_cart, locatorType="xpath")
        self.waitForElement(locator=self._go_to_fulfill_the_order_button, locatorType="xpath")

    def getFewProductsToCart(self, quantity):
        self.getProductToCartPanda(quantity)
        self.elementClick(locator=self._continue_shopping_button, locatorType="xpath")
        self.waitForElement(locator=self._select_size, locatorType="name")
        time.sleep(2)
        self.getProductToCartFiona(quantity)
        self.elementClick(locator=self._go_to_fulfill_the_order_button, locatorType="xpath")
        self.waitForElement(locator="cart-detailed-totals",locatorType="class")

    def getFewProductsToCartSuccessful(self, quantity):
        self.getFewProductsToCart(quantity)
        num = self.driver.find_element(By.XPATH, self._num_of_products_in_cart).text
        if str((quantity*2)) in str(num):
            result = True
        else:
            result = False
        return result

    def priceOfProductsInBasket(self,quantity):
        self.getFewProductsToCart(quantity)
        elements = self.driver.find_elements(By.XPATH, "//div[@class='current-price']/span[@class='price']")
        prices = []
        for el in elements:
            price = el.text
            price = price.replace("zł", "")
            price = price.replace(",",".")
            price = price.rstrip()
            price = float(price)
            price = format(price,".2f")
            prices.append(price)
        numOfProducts = self.driver.find_elements(By.NAME, "product-quantity-spin")
        numsOfProducts = []
        for num in numOfProducts:
            number = num.get_attribute("value")
            number = float(number)
            number = format(number,".2f")
            numsOfProducts.append(number)
        multiplyProducts = []
        for i in range(0,len(prices)):
            multiply = float(numsOfProducts[i])*float(prices[i])
            multiplyProducts.append(multiply)
        sumOfProducts = sum(multiplyProducts)
        sumOfProductss = format(sumOfProducts,".2f")
        sumNum = self.driver.find_element(By.XPATH, "//div[@id='cart-subtotal-products']/span[@class='value']").text.replace("zł","")
        sumNum = sumNum.replace(",",".")
        if float(sumOfProductss) == float(sumNum):
            result = True
        else:
            result = False
        return result

    def deleteFromCart(self):
        self.getFewProductsToCart(quantity=1)
        self.elementClick(locator=self._go_to_fulfill_the_order_button, locatorType="xpath")
        self.waitForElement(locator="cart-detailed-totals", locatorType="class")
        quantityOfProducts = self.driver.find_elements(By.XPATH, self._products_in_cart)
        quantity1 = len(quantityOfProducts)
        self.elementClick(locator=self._first_product_trashcan, locatorType="xpath")
        time.sleep(2)
        quantityOfProducts2 = self.driver.find_elements(By.XPATH, self._products_in_cart)
        quantity2 = len(quantityOfProducts2)
        if quantity1 > quantity2:
            result = True
        else:
            result = False
        return result

    def changeQuantity(self):
        self.getProductToCartPanda(quantity=2)
        self.elementClick(locator=self._go_to_fulfill_the_order_button, locatorType="xpath")
        self.waitForElement(locator="cart-detailed-totals", locatorType="class")
        firstPrice = self.driver.find_element(By.XPATH, "//div[@id='cart-subtotal-products']/span[@class='value']").text
        price1 = firstPrice.replace("zł", "")
        price1 = price1.replace(",",".")
        price1 = float(price1)
        price1 = format(price1, ".2f")
        self.elementClick(locator=self._touchspin_down, locatorType="xpath")
        time.sleep(2)
        secondPrice = self.driver.find_element(By.XPATH, "//div[@id='cart-subtotal-products']/span[@class='value']").text
        price2 = secondPrice.replace("zł", "")
        price2 = price2.replace(",",".").rstrip()
        price2 = float(price2)
        price2 = format(price2,".2f")
        if float(price1) > float(price2):
            result = True
        else:
            result = False
        return result



















