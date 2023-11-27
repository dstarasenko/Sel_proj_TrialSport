import time
from selenium import webdriver

from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.mountain_ski_page import Mountain_ski_page


def test_select_products():
    driver = webdriver.Chrome()
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors-spki-list')
    options.add_argument('--ignore-ssl-errors')

    mp = Main_page(driver)
    mp.authorization()

    time.sleep(1)

    cp = Catalog_page(driver)
    cp.mountain_ski_in_catalog()

    time.sleep(1)

    msp = Mountain_ski_page(driver)
    msp.mountain_ski_filters()

    time.sleep(5)