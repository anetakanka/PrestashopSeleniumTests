from pages.clothes_page.product_page import ProductPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures('oneTimeSetUp', 'setUp')
class ProductTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.pp = ProductPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_productTitle(self):
        self.log.info("Verify the title of product")
        result = self.pp.productTitle(title="t-shirt panda")
        assert result == True

    @pytest.mark.run(order=2)
    def test_productDescription(self):
        self.log.info("Verify product description")
        description = "Koszulka z krótkim rękawem i nadrukiem z pandą"
        result = self.pp.productDescription(description)
        assert result == True

    @pytest.mark.run(order=3)
    def test_imgDisplayed(self):
        self.log.info("Check that the image is displayed")
        result = self.pp.imgDisplayed()
        assert result == True

    @pytest.mark.run(order=4)
    def test_imgEnlarged(self):
        self.log.info("check if the picture is enlarged or not")
        result = self.pp.imgEnlarge()

    @pytest.mark.run(order=5)
    def test_sizeNotAvailable(self):
        self.log.info("Verifies the availability of an unavailable size")
        result = self.pp.sizeNotAvailable()
        assert result == True

