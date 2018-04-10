import utilities.custom_logger as cl
from selenium.webdriver.common.by import By
import logging
from base.basepage import BasePage
from pages.home_page.navigation import NavigationPage
from pages.home_page.login_page import LoginPage
from pages.cart_page.cart_page import CartPage
import time


class CheckoutPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.cp = CartPage(self.driver)

    #Loctors
    _go_to_fulfill_the_order_button = "//div[@class='modal-content']//a"  # byxpath
    _proceed_to_order_completion = "PRZEJDŹ DO REALIZACJI ZAMÓWIENIA" #bylink
    _checkout_form = "checkout-personal-information-step" #byid
    # for visitor client
    _gender = "//div[@class='col-md-6 form-control-valign']/label[1]//input[@name='id_gender']"#byxpath gender = men
    _address_checkout_form = "//div[@class='js-address-form'][1]" #byxpath #pojawia się gdy poprawnie wypełni się pierwszy formularz
    _firstname = "firstname" #byname
    _lastname = "lastname" #byname
    _email = "//input[@name='email'][1]" #byxpath
    _password = "//input[@name='password'][1]" #byxpath
    _submit_first_form = "//button[@name='continue'][1]" #byxpath
    _wrong_email_info = "//form[@id='customer-form']//ul/li[@class='alert alert-danger']" #byxpath
    _address = "address1" #byname
    _postcode = "postcode" #byname
    _city = "city" #byname
    _phone = "phone" #byname
    _confirm_addresses = "confirm-addresses" #byname
    _alert_inf_address = "//div[@id='delivery-address']//ul/li[@class='alert alert-danger']" #byxpath
    _delivery_option2 = "delivery_option_2" #byid
    _delivery_message = "delivery_message" #byid
    _confirm_delivery_option = "confirmDeliveryOption" #byname
    _payment_option2 = "payment-option-2" #byid
    _conditions_acceptance = "conditions_to_approve[terms-and-conditions]" #byid bez togo nie można kliknąć payment confirmation sprawdz!
    _payment_confirmation = "//div[@id='payment-confirmation']//button[@type='submit']" #byxpath
    #for logged in client
    _personal_inf = "//section[@id='checkout-personal-information-step']/h1" #byxpath
    _user_name = "//a[@href='http://localhost/prestashop/dane-osobiste']" #byxpath
    _address2 = "//div[@class='address'][1]" #byxpath
    _add_new_address = "//a[@href='http://localhost/prestashop/zamówienie?newAddress=delivery']" #byxpath

    def goToCheckout(self):
        self.cp.getProductToCartFiona(quantity=1)
        self.elementClick(locator=self._go_to_fulfill_the_order_button, locatorType="xpath")
        self.waitForElement(locator="cart-detailed-totals", locatorType="class")
        self.elementClick(locator=self._proceed_to_order_completion, locatorType="link")
        self.waitForElement(locator=self._checkout_form)

    def checkoutGuestFormPersonalInformation(self,firstname, lastname, email, password):
        self.goToCheckout()
        time.sleep(2)
        self.elementClick(locator=self._gender, locatorType="xpath")
        self.sendKeys(firstname, locator=self._firstname, locatorType="name")
        self.sendKeys(lastname, locator=self._lastname, locatorType="name")
        self.sendKeys(email, locator=self._email, locatorType="xpath")
        self.sendKeys(password, locator=self._password, locatorType="xpath")
        self.elementClick(locator=self._submit_first_form, locatorType="xpath")

    def checkoutGuestFormPersonalInformationSuccessful(self, firstname, lastname,email,password):
        self.checkoutGuestFormPersonalInformation(firstname, lastname, email, password)
        self.waitForElement(locator=self._address_checkout_form, locatorType="xpath")
        result = self.isElementPresent(locator=self._address_checkout_form, locatorType="xpath")
        return result

    def checkoutGuestFormPersonalInformationFailed(self,firstname, lastname, email, password):
        # providing a wrong email address
        self.checkoutGuestFormPersonalInformation(firstname, lastname, email, password)
        self.waitForElement(locator=self._wrong_email_info, locatorType="class")
        result = self.isElementPresent(locator=self._wrong_email_info, locatorType="xpath")
        return result

    def addressForm(self, firstname, lastname, email, password, address, postcode, city, phone):
        self.checkoutGuestFormPersonalInformation(firstname,lastname,email,password)
        self.waitForElement(locator=self._address_checkout_form, locatorType="xpath")
        self.sendKeys(address, locator=self._address, locatorType="name")
        self.sendKeys(postcode, locator=self._postcode, locatorType="name")
        self.sendKeys(city, locator=self._city, locatorType="name")
        self.sendKeys(phone, locator=self._phone, locatorType="name")
        self.elementClick(locator=self._confirm_addresses, locatorType="name")

    def addressFormSuccessful(self, firstname, lastname, email, password, address, postcode, city, phone):
        self.addressForm( firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator="checkout-delivery-step")
        result = self.isElementPresent(locator="checkout-delivery-step")
        return result

    def addressFormFailed(self, firstname, lastname, email, password, address, postcode, city, phone):
        self.addressForm(firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator=self._alert_inf_address, locatorType="class")
        result = self.isElementPresent(locator=self._alert_inf_address, locatorType="xpath")
        return result

    def delivery(self, firstname, lastname, email, password, address, postcode, city, phone):
        self.addressForm(firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator="checkout-delivery-step")
        self.elementClick(locator=self._delivery_option2)
        self.elementClick(locator=self._confirm_delivery_option, locatorType="name")

    def deliverySuccessed(self,firstname, lastname, email, password, address, postcode, city, phone):
        self.delivery(firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator=self._payment_option2)
        result = self.isElementPresent(locator=self._payment_option2)
        return result

    def payment(self,firstname, lastname, email, password, address, postcode, city, phone):
        self.delivery(firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator=self._payment_option2)
        self.elementClick(locator=self._payment_option2)

    def paymentConditionsAcceptanceVerification(self, firstname, lastname, email, password, address, postcode, city, phone):
        self.payment(firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator=self._payment_confirmation, locatorType="xpath")
        self.elementClick(locator=self._payment_confirmation, locatorType="xpath")
        element = self.getElement(locator=self._payment_confirmation, locatorType="xpath")
        result = element.is_enabled()
        if result == False:
            return True
        return False

    def paymentSuccessed(self, firstname, lastname, email, password, address, postcode, city, phone):
        self.payment( firstname, lastname, email, password, address, postcode, city, phone)
        self.waitForElement(locator=self._conditions_acceptance)
        self.elementClick(locator=self._conditions_acceptance)
        self.elementClick(locator=self._payment_confirmation, locatorType="xpath")
        self.waitForElement(locator="order-confirmation-table", locatorType="class")
        result = self.isElementPresent(locator="order-confirmation-table", locatorType="class")
        return result

    def checkoutLoggedInClient(self, email, password):
        self.lp.login(email,password)
        self.goToCheckout()

    def personalInfVeryficationLoggedinClient(self, username, email, password):
        self.checkoutLoggedInClient(email, password)
        self.waitForElement(locator=self._personal_inf, locatorType="xpath")
        self.elementClick(locator=self._personal_inf, locatorType="xpath")
        self.waitForElement(locator=self._user_name, locatorType="xpath")
        username1 = self.getElement(locator=self._user_name, locatorType="xpath").text
        if username == username1:
            result = True
        else:
            result = False
        return result

    def addressVeryficationLoggedinClient(self, address, email, password):
        #w tescie zrób go to main page i wyloguj najpierw
        self.checkoutLoggedInClient(email,password)
        self.waitForElement(locator=self._address2, locatorType="class")
        element = self.getElement(locator=self._address2, locatorType="xpath")
        address1 = element.text
        if address1 == address:
            result = True
        else:
            result = False
        return result

    def addNewAddressLoggedinClient(self, email, password, address, postcode, city, phone):
        self.checkoutLoggedInClient(email, password)
        self.waitForElement(locator=self._address2, locatorType="class")
        self.elementClick(locator=self._add_new_address, locatorType="xpath")
        self.sendKeys(address, locator=self._address, locatorType="name")
        self.sendKeys(postcode, locator=self._postcode, locatorType="name")
        self.sendKeys(city, locator=self._city, locatorType="name")
        self.sendKeys(phone, locator=self._phone, locatorType="name")
        self.elementClick(locator=self._confirm_addresses, locatorType="name")
        self.waitForElement(locator="checkout-delivery-step")
        result = self.isElementPresent(locator="checkout-delivery-step")
        return result





















