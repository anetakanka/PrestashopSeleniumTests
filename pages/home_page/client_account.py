import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
import time

class AccountPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//div[@class='user-info']//span[contains(text(), 'Zaloguj')]"
    _create_account = "No account? Create one here" #bylinktext
    _register_form = 'register-form' #by class
    _gender = "//input[@name='id_gender'][1]" #byxpath
    _firstname = "firstname" #byname
    _lastname = "lastname" #byname
    _email = "//form[@id='customer-form']//input[@name='email']" #byxpath
    _password = "password" #byname
    _submit_form = "//form[@id='customer-form']//button[@type='submit']" #byxpath
    _user_info_field = "user-info" #byclass
    _alert = "//div[@class='help-block']//li[@class='alert alert-danger']" #by xpath

    # def registerFormElementsValidation(self):
    #     self.elementClick(locator=self._login_link, locatorType="xpath")
    #     self.waitForElement(locator=self._create_account, locatorType="link")
    #     self.elementClick(locator=self._create_account, locatorType="link")
    #     self.waitForElement(locator=self._register_form, locatorType="class")
    #     email = self.driver.execute_script("return document.getElementByName(\"email\")[0].validity.valid")
    #     password = self.driver.execute_script("return document.getElementByName(\"password\")[0].validity.valid")
    #     if email and password:
    #         return True
    #     return False

    def createNewAccount(self,firstname,lastname,email,password,):
        self.elementClick(locator=self._login_link, locatorType="xpath")
        self.waitForElement(locator=self._create_account, locatorType="link")
        self.elementClick(locator=self._create_account, locatorType="link")
        self.waitForElement(locator=self._register_form, locatorType="class")
        self.elementClick(locator=self._gender, locatorType="xpath")
        self.sendKeys(data=firstname, locator=self._firstname, locatorType="name")
        self.sendKeys(data=lastname, locator=self._lastname, locatorType="name")
        self.clearField(locator=self._email, locatorType="xpath")
        self.sendKeys(data=email, locator=self._email, locatorType="xpath")
        self.clearField(locator=self._password,locatorType="name")
        self.sendKeys(data=password,locator=self._password,locatorType="name")
        self.elementClick(locator=self._submit_form, locatorType="xpath")

    def createNewAccountFailed(self, firstname,lastname,email,password):
        self.createNewAccount(firstname,lastname,email,password)
        self.waitForElement(locator=self._alert,locatorType="xpath")
        result = self.isElementPresent(locator=self._alert,locatorType="xpath")
        return result

    def createNewAccountSuccessful(self,firstname,lastname,email,password):
        self.createNewAccount(firstname,lastname,email,password)
        self.waitForElement(locator=self._user_info_field, locatorType="class")
        result = self.isElementPresent(locator=self._user_info_field, locatorType="class")
        return result



