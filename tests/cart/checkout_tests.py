from base.selenium_driver import SeleniumDriver
from pages.cart_page.checkout_page import CheckoutPage
from utilities.teststatus import TestStatus
from pages.home_page.navigation import NavigationPage
from pages.home_page.login_page import LoginPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class CheckoutTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.chp = CheckoutPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)
        self.sd = SeleniumDriver(self.driver)

    @pytest.mark.run(order=1)
    def test_checkoutGuestFormPersonalInformationSuccessful(self):
        self.log.info("Personal Information form for guest client successed")
        email = email = "test" + str(round(time.time() * 1000)) +"@test.com"
        result = self.chp.checkoutGuestFormPersonalInformationSuccessful(firstname="Adam",lastname="Kowalski",
                                                                         email=email, password="abcabc123")
        assert result == True

    @pytest.mark.run(order=2)
    def test_checkoutGuestFormPersonalInformationFailed(self):
        self.log.info("Personal Information form for guest client failed due to wrong email")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        result = self.chp.checkoutGuestFormPersonalInformationFailed(firstname="Adam",lastname="Kowalski",
                                                                         email="test@test.com", password="abcabc123")
        assert result == True

    @pytest.mark.run(order=3)
    def test_addressFormSuccessful(self):
        self.log.info("Address form for guest client successful")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.chp.addressFormSuccessful(firstname="Adam",lastname="Kowalski",email=email, password="abcabc123",
                                       address="Testowa 1/2", postcode="00-000", city="Warszawa", phone="500500500")
        assert result == True

    @pytest.mark.run(order=4)
    def test_addressFormFailed(self):
        self.log.info("Address form for guest client failed due to wrong postcode")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.chp.addressFormFailed(firstname="Adam",lastname="Kowalski",email=email, password="abcabc123",
                                       address="Testowa 1/2", postcode="00", city="Warszawa", phone="500500500")
        assert result == True

    @pytest.mark.run(order=5)
    def test_addressFormFailed2(self):
        self.log.info("Address form for guest client failed due to wrong phone number")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.chp.addressFormFailed(firstname="Adam", lastname="Kowalski", email=email, password="abcabc123",
                                            address="Testowa 1/2", postcode="00-000", city="Warszawa", phone="abc")
        assert result == True

    @pytest.mark.run(order=6)
    def test_deliverySuccessed(self):
        self.log.info("Delivery form successed")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.chp.deliverySuccessed(firstname="Adam",lastname="Kowalski",email=email, password="abcabc123",
                                       address="Testowa 1/2", postcode="00-000", city="Warszawa", phone="500500500")
        assert result == True

    @pytest.mark.run(order=7)
    def test_paymentConditionsAcceptanceVerification(self):
        self.log.info("Payment conditions acceptance verification successful")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.chp.paymentConditionsAcceptanceVerification(firstname="Adam",lastname="Kowalski",email=email,
                                                                  password="abcabc123",address="Testowa 1/2",
                                                                  postcode="00-000", city="Warszawa", phone="500500500")
        assert result == True

    @pytest.mark.run(order=8)
    def test_paymentSuccessed(self):
        self.log.info("Address form for guest client successful")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.chp.paymentSuccessed(firstname="Adam",lastname="Kowalski",email=email, password="abcabc123",
                                       address="Testowa 1/2", postcode="00-000", city="Warszawa", phone="500500500")
        assert result == True

    @pytest.mark.run(order=9)
    def test_personalInfVerificationLoggedInClient(self):
        self.log.info("Personal information form for logged in client verification successful")
        self.nav.clearCartAndGoToMainPage()
        self.lp.logOut()
        result = self.chp.personalInfVerificationLoggedInClient(username="Ewa Kowalska", email="test3@test.com",
                                                       password="abcabc123")
        assert result == True

    @pytest.mark.run(order=10)
    def test_addressVerificationLoggedInClient(self):
        self.log.info("Address form for logged in client successful")
        self.nav.backToHomePage()
        self.lp.logOut()
        address = "Ewa Kowalska\nul. Testowa\n00-000 Warszawa\nPolska\n600600600"
        result = self.chp.addressVerificationLoggedInClient(address=address, email="test3@test.com", password="abcabc123")
        assert result == True

    @pytest.mark.run(order=10)
    def test_addNewAddressLoggedInClient(self):
        self.log.info("Add address form for logged in client successful")
        self.nav.backToHomePage()
        self.lp.logOut()
        address = "Testowa" + str(round(time.time() * 1000)) + "/2"
        result = self.chp.addNewAddressLoggedinClient(email="test3@test.com", password="abcabc123", address=address,
                                             postcode="00-000", city="Warszawa", phone="600600600")
        assert result == True
        self.ts.markFinal("test_addNewAddressLoggedinClient", result, "Add address form for logged in client successful"
                                                                   "verification SUCCESSED")



