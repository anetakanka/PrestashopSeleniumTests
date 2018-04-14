import utilities.custom_logger as cl
import logging
from base.basepage import BasePage
from pages.home_page.navigation import NavigationPage
import time

class ContactPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _contact_page = "link-static-page-contact-2]" #byID
    _contact_form = "contact-form" #byclass
    _contact_address = "data" #byclass
    _contact_email = "//div[@id='left-column']//a[@href='mailto:obslugaklienta@blackwhite.com']" #byxpath
    _subject_list = "id_contact" #byname
    _subject_1 = "//select[@name='id_contact']//option[1]" #byxpath
    _email = "from" #byname
    _message = "message" #byname
    _send = "submitMessage" #byname
    _contact_number = "500500500" #bylink
    _contact_failed ="//section[@id='content']//li[contains(text(),'Wiadomość nie może być pusta')]" #byxpath
    _contact_success= "//section[@id='content']//li[contains(text(),'Twoja wiadomość została pomyślnie wysłana do obsługi.')]" #byxpath
    _newsletter_email_input = "email" #byname
    _submit_newsletter = "//input[@name='submitNewsletter'][1]" #byxpath
    _submit_newsletter_success = "//p[contains(text(), 'Zarejestrowano do subskrypcji')]" #byxpath
    _submit_newsletter_failed = "//p[contains(text(), 'Ten email już jest w bazie')]" #byxpath
    _maine_page_phonenumber = "//div[@id='contact-link']/span" #byxpath

    def contactEmail(self, contactemail):
        self.nav.goToContactPage()
        contact_email = self.getElement(locator=self._contact_email, locatorType="xpath")
        email = contact_email.text
        if email == contactemail:
            result = True
        else:
            result = False
        return result

    def contactAddress(self,address):
        self.nav.goToContactPage()
        caddress = self.getElement(locator=self._contact_address, locatorType="class")
        contactAddress = caddress.text.lower()
        if contactAddress == address:
            result = True
        else:
            result = False
        return result

    def contactNumber(self, phonenumber):
        self.nav.goToContactPage()
        cnumber = self.getElement(locator=self._contact_number, locatorType="link")
        contactNumber = cnumber.text
        if contactNumber == phonenumber:
            result = True
        else:
            result = False
        return result

    def contactForm(self, email, message):
        self.nav.goToContactPage()
        self.elementClick(locator=self._subject_list, locatorType="name")
        self.waitForElement(locator=self._subject_1, locatorType="xpath")
        self.elementClick(locator=self._subject_1, locatorType="xpath")
        self.sendKeys(email, locator=self._email, locatorType="name")
        self.sendKeys(message, locator=self._message, locatorType="name")
        self.elementClick(locator=self._send, locatorType="name")

    def contactFormSuccess(self, email, message):
        self.contactForm(email, message)
        self.waitForElement(locator=self._contact_success, locatorType="xpath")
        result = self.isElementPresent(locator=self._contact_success, locatorType="xpath")
        return result

    def contactFormFailed(self,email,message):
        self.contactForm(email,message)
        self.waitForElement(locator=self._contact_failed, locatorType="xpath")
        result = self.isElementPresent(locator=self._contact_failed, locatorType="xpath")
        return result

    def newsletter(self, email):
        self.nav.goToContactPage()
        self.sendKeys(email, locator=self._newsletter_email_input, locatorType="name")
        self.elementClick(locator=self._submit_newsletter, locatorType="xpath")

    def newsletterSuccessed(self, email):
        self.newsletter(email)
        self.waitForElement(locator=self._submit_newsletter_success, locatorType="xpath")
        result = self.isElementPresent(locator=self._submit_newsletter_success, locatorType="xpath")
        return result

    def newsletterFailed(self, email):
        self.newsletter(email)
        self.waitForElement(locator=self._submit_newsletter_failed, locatorType="xpath")
        result = self.isElementPresent(locator=self._submit_newsletter_failed, locatorType="xpath")
        return result

    def maincontactNumber(self, number):
        num = self.getElement(locator=self._maine_page_phonenumber, locatorType="xpath")
        cnum = num.text
        if cnum == number:
            result = True
        else:
            result = False
        return result


