from pages.home_page.client_account import AccountPage
from utilities.teststatus import TestStatus
from pages.home_page.navigation import NavigationPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class AccountTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.ap = AccountPage(self.driver)
        self.ts = TestStatus(self.driver)
        self.nav = NavigationPage(self.driver)

    # @pytest.mark.run(order=1)
    # def test_registerFormElementsValidation(self):
    #     self.log.info("Validation of elements of a customer registration form successful")
    #     result = self.ap.registerFormElementsValidation()
    #     assert result == True

    @pytest.mark.run(order=2)
    def test_createNewAccountFailedEmail(self):
        self.nav.backToHomePage()
        self.log.info("Created a new customer account unsuccessful by providing an invalid email address")
        result = self.ap.createNewAccountFailed(firstname="Jan", lastname="Kowalski",
                                                email="test@test.com", password="abcabc123")
        assert result ==True

    @pytest.mark.run(order=3)
    def test_createNewAccountFailedFirstname(self):
        self.nav.backToHomePage()
        email = "test" + str(round(time.time() * 1000)) +"@test.com"
        self.log.info("Created a new customer account unsuccessful by providing an invalid firstname")
        result = self.ap.createNewAccountFailed(firstname="123@$", lastname="Kowalski",
                                                email=email, password="abcabc123")
        assert result == True

    @pytest.mark.run(order=4)
    def test_createNewAccountFailedLastname(self):
        self.nav.backToHomePage()
        email = "test" + str(round(time.time() * 1000)) + "@test.com"
        self.log.info("Created a new customer account unsuccessful by providing an invalid firstname")
        result = self.ap.createNewAccountFailed(firstname="Jan", lastname="$@23",
                                                email=email, password="abcabc123")
        assert result == True

    @pytest.mark.run(order=5)
    def test_createNewAccountSuccessful(self):
        self.nav.backToHomePage()
        self.log.info("Created a new customer account successful")
        email = "test" + str(round(time.time() * 1000)) +"@test.com"
        result = self.ap.createNewAccountSuccessful(firstname="Jan", lastname="Kowalski",
                                                    email=email, password="abcabc123")
        assert result == True
        self.ts.markFinal("test_createNewAccountSuccessful", result, "Created a new customer account successful "
                                                                   "verification SUCCESSED")
