import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from base.selenium_driver import SeleniumDriver


class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "//div[@class='user-info']//span[contains(text(), 'Zaloguj')]"
    _email_field = "//div[@class='col-md-6']//input[@name='email']"
    _password_field = "password" # ByName
    _login_submit_button = "submit-login" #ByID
    _login_failed_message = "//div[@class='help-block']//li[@class='alert alert-danger']" #byXpath
    _logout_button = "//div[@id='_desktop_user_info']//a[@class='logout hidden-sm-down']" #byXpath
    _desactivated_account_info = "//section[@id='content']//li[contains(text(),'Twoje konto nie jest w tej chwili aktywne, skontaktuj się z nami')]" #byxpath

    def clickLoginLink(self):
        self.elementClick(locator=self._login_link, locatorType='xpath')

    def enterEmail(self, email):
        self.sendKeys(email, locator=self._email_field, locatorType='xpath')

    def enterPassword(self, password):
        self.sendKeys(password, locator=self._password_field, locatorType='name')

    def clickLoginButton(self):
        self.elementClick(locator=self._login_submit_button)

    def login(self, email="", password=""):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        self.waitForElement(locator=self._logout_button, locatorType='xpath')
        result = self.isElementPresent(self._logout_button, locatorType='xpath')
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent(locator=self._login_failed_message, locatorType='xpath')
        return result

    def logout(self):
        self.elementClick(locator=self._logout_button, locatorType='xpath')

    def emailValidation(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.waitForElement(locator=self._email_field, locatorType="xpath", pollFrequency=1)
        result = self.driver.execute_script("return document.getElementsByName(\"email\")[0].validity.valid")
        return result

    def passwordValidation(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.waitForElement(locator=self._password_field, locatorType="name", pollFrequency=1)
        result = self.driver.execute_script("return document.getElementsByName(\"password\")[0].validity.valid")
        return result

    def logOut(self):
        self.elementClick(locator=self._logout_button, locatorType='xpath')

    def deactivatedCustomerAccountLogin(self, email,password):
        self.login(email,password)
        self.waitForElement(locator=self._desactivated_account_info, locatorType="xpath")
        result = self.isElementPresent(locator=self._desactivated_account_info, locatorType="xpath")
        return result


