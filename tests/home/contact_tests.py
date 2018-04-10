from pages.home_page.contact_page import ContactPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class ContactTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.cp = ContactPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_contactEmail(self):
        self.log.info("verifies that the e-mail address is correct")
        result = self.cp.contactEmail(contactemail="obslugaklienta@blackwhite.com")
        assert result == True

    @pytest.mark.run(order=2)
    def test_contactNumber(self):
        self.log.info("verifies that the contact phone number is correct")
        result = self.cp.contactNumber(phonenumber="500500500")
        assert result == True

    @pytest.mark.run(order=3)
    def test_mainContactNumber(self):
        self.log.info("verifies that the contact phone number on main site is correct")
        result = self.cp.maincontactNumber(number="500500500")
        assert result == True

    @pytest.mark.run(order=4)
    def test_contactAddress(self):
        self.log.info("verifies that the contact address is correct")
        address = "black&white\nulica 1/1\n00-000 warszawa\npolska"
        result = self.cp.contactAddress(address)
        assert result == True

    @pytest.mark.run(order=5)
    def test_contactFormSuccesssed(self):
        self.log.info("Check that the contact form is working correctly")
        message = open("sample.txt", "r", encoding="utf-8")
        message1 = message.read()
        result = self.cp.contactFormSuccess(email="test3@test.com", message=message1)
        assert result == True

    @pytest.mark.run(order=6)
    def test_contactFormFailed(self):
        self.log.info("Check that the contact form is working correctly")
        result = self.cp.contactFormFailed(email="test3@test.com", message="")
        assert result == True

    @pytest.mark.run(order=7)
    def test_newsletterSuccessed(self):
        self.log.info("Check if subscribing to the newsletter is working properly")
        email = email = "test" + str(round(time.time() * 1000)) + "@test.com"
        result = self.cp.newsletterSuccessed(email=email)
        assert result == True

    @pytest.mark.run(order=8)
    def test_newsletterFailed(self):
        self.log.info("Check if subscribing to the newsletter is working properly")
        result = self.cp.newsletterFailed(email="test@test.com")
        assert result == True













