from pages.home_page.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
from ddt import ddt, data, unpack
from utilities.read_cvs_data import getCSVData


@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
@ddt
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    @data(*getCSVData("invalidLogin.csv"))
    @unpack
    def test_invalidPasswordLogin(self, email, password):
        self.log.info("Test invalid login")
        self.lp.login(email, password)
        result = self.lp.verifyLoginFailed()
        assert result == True

    @pytest.mark.run(order=2)
    def test_emailInputValidationFailed(self):
        # Check email input element validation based on the pattern
        self.log.info("Test email input validation")
        result = self.lp.emailValidation(email='testtest.com', password='abcabc123')
        assert result == False

    @pytest.mark.run(order=3)
    def test_emailInputValidationSuccessed(self):
        # Check email input element validation based on the pattern
        self.log.info("Test email input validation failed")
        result = self.lp.emailValidation(email='test@test.com', password='abcabc123')
        assert result == True

    @pytest.mark.run(order=4)
    def test_passwordInputValidationFailed(self):
        # Check password input element validation based on the pattern
        self.log.info("Test password input validation failed")
        result = self.lp.passwordValidation(email='test@test.com', password='abc')
        assert result == False

    @pytest.mark.run(order=5)
    def test_passwordInputValidationSuccessed(self):
        # Check password input element validation based on the pattern
        self.log.info("Test password input validation successed")
        result = self.lp.passwordValidation(email='test@test.com', password='abcabc123')
        assert result == True

    @pytest.mark.run(order=6)
    def test_deactivatedCustomerAccountLogin(self):
        result = self.lp.deactivatedCustomerAccountLogin(email="test2@test.com", password="abcabc123")
        assert result == True

    @pytest.mark.run(order=7)
    def test_successfulLogin(self):
        self.log.info("Test successful login")
        self.lp.login("test@test.com", "abcabc123")
        result = self.lp.verifyLoginSuccessful()
        assert result == True
        self.ts.markFinal("test_successfulLogin", result, "Login verification SUCCESSED")