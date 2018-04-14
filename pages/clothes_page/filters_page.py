import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import logging
from base.basepage import BasePage
from pages.home_page.navigation import NavigationPage
from selenium.webdriver import ActionChains
import time


class FiltersPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    #Loctors
    _clothes_page = "//a[@href='http://localhost/prestashop/3-clothes']"#by xpath
    _men_page = '//ul[@class="category-sub-menu"]//a[contains(text(),"Men")]' #byXpath
    _man_collapse_menu = '//div[@id="left-column"]//ul[@class="category-sub-menu"]/li[1]/div[1]]' #byXpath
    _woman_page = '//ul[@class="category-sub-menu"]//a[@href="http://localhost/prestashop/5-women"]' #byXpath
    _woman_collapse_menu = '//div[@id="left-column"]//ul[@class="category-sub-menu"]/li[2]/div[1]' #byXpath
    _woman_collapse_menu_bluzki = '//ul[@class="category-sub-menu"]/li[2]//ul[@class="category-sub-menu"]//a[contains(text(),"Bluzki")]'
    # clothes
        #sizes:
    _size_S = '//div[@id="search_filters"]/section[2]/ul/li[1]//span[@class="custom-checkbox"]'
    _size_M = '//div[@id="search_filters"]/section[2]/ul/li[2]//span[@class="custom-checkbox"]'
    _size_L = '//div[@id="search_filters"]/section[2]/ul/li[3]//span[@class="custom-checkbox"]'
    _size_XL = '//div[@id="search_filters"]/section[2]/ul/li[4]//span[@class="custom-checkbox"]'
        #colors:
    _white_color = '//div[@id="search_filters"]/section[3]/ul/li[1]//span[@class="custom-checkbox"]/input'
    _black_color = '//div[@id="search_filters"]/section[3]/ul/li[2]//span[@class="custom-checkbox"]/input'
        #prices:
    _price_cat1 = '//div[@id="search_filters"]/section[4]/ul/li[1]//span[@class="custom-checkbox"]'
    _price_cat2 = '//div[@id="search_filters"]/section[4]/ul/li[2]//span[@class="custom-checkbox"]'
    _price_cat3 = '//div[@id="search_filters"]/section[4]/ul/li[3]//span[@class="custom-checkbox"]'
    _price_cat4 = '//div[@id="search_filters"]/section[4]/ul/li[4]//span[@class="custom-checkbox"]'

    def goToMenPageSuccessful(self):
        self.nav.goToClothesPage()
        self.elementClick(locator=self._men_page, locatorType='xpath')
        self.waitForElement(locator='//div[@class="block-category card card-block hidden-sm-down"]/h1[contains(text(), "Men")]',
                            locatorType='xpath')
        result = self.isElementPresent(locator='//div[@class="block-category card card-block hidden-sm-down"]/h1[contains(text(), "Men")]',
                                       locatorType='xpath')
        return result

    def clothesWomenBluzkiPage(self):
        self.waitForElement(locator="//div[@id='js-product-list']/div[@class='products row']/article[1]")
        products = self.driver.find_elements(By.XPATH,
                                             "//div[@id='js-product-list']/div[@class='products row']//h1[@class='h3 product-title']/a")
        for el in products:
            product = el.text
            if 'Bluzka' not in product:
                return False
        return True


    def clothesPagehoverOverMenu(self):
        self.nav.backToHomePage()
        element = self.driver.find_element(By.XPATH, self._clothes_page)
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        self.waitForElement(locator="//ul[@id='top-menu']/li[1]/div", locatorType="xpath")
        self.elementClick(locator="//ul[@id='top-menu']/li[1]/div/ul/li[2]//a[contains(text(),'Bluzki')]", locatorType="xpath")

    def collapseMenuWomenBlouse(self):
        self.nav.goToClothesPage()
        self.waitForElement(locator=self._woman_collapse_menu, locatorType="xpath")
        self.elementClick(locator=self._woman_collapse_menu, locatorType="xpath")
        self.waitForElement(locator=self._woman_collapse_menu_bluzki, locatorType='xpath')
        self.elementClick(locator=self._woman_collapse_menu_bluzki, locatorType='xpath')

    def multipleFiltersClick(self):
        # Clicks on the color and size clothes
        self.nav.goToClothesPage()
        self.driver.execute_script("window.scrollBy(0, -300);")
        self.waitForElement(locator='search_filters')
        self.elementClick(locator=self._size_M, locatorType='xpath')
        time.sleep(2)
        self.elementClick(locator=self._black_color, locatorType='xpath')
        time.sleep(2)

    def multipleFiltersSuccessful(self):
        # Checks if selected products are the same as products in database
        products = []
        text_list = []
        product_list = self.driver.find_elements(By.XPATH,
                                                    "//div[@class='products row']/article//h1[@class='h3 product-title']/a")
        for product in product_list:
            hr = product.text
            text_list.append(hr.lower())
        file = open("product_list_black_m.txt", "r", encoding="utf-8")
        product_list_database = file.readlines()
        for line in product_list_database:
            el = line.rstrip()
            products.append(el.lower())
        for line in products:
            if line not in text_list:
                return False
        return True









