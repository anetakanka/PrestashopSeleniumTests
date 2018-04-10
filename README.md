#Prestashop Selenium Tests

Project includes a framework and sample tests that are covering the main functionalities of the Black&white shop. The shop is build on the prestashop, in the default template for the clothing shop.
Code is written in python and selenium.

##Requirements:
    *Python 3.6.3,
    *Pytest-3.4.2,
    *Selenium
    *At least one of the browsers: Chrome, Firefox, InternetExplorer

## Usage

1) Clone this repository.
2) Install all dependencies(paragraph above)
3. To run all test - write in command line: py.tests tests\test_suite.py --browser "selected browser"
4. To run particular test - write in command line: py.tests (path to test) -- browser "selected browser"
