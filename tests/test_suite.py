import unittest
from tests.cart.cart_tests import CartTests
from tests.cart.checkout_tests import CheckoutTests
from tests.clothes.discount_tests import DiscountTests
from tests.clothes.filters_tests import FiltersTests
from tests.clothes.product_tests import ProductTests
from tests.home.account_tests import AccountTests
from tests.home.contact_tests import ContactTests
from tests.home.login_tests import LoginTests
from tests.home.search_tests import SearchTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ContactTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(SearchTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(FiltersTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(ProductTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(DiscountTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(CartTests)
tc8 = unittest.TestLoader().loadTestsFromTestCase(AccountTests)
tc9 = unittest.TestLoader().loadTestsFromTestCase(CheckoutTests)

BlackWhiteTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8, tc9])

unittest.TextTestRunner(verbosity=2).run(BlackWhiteTest)


