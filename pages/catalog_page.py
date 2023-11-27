import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base

""" 
    Главная страница магазина Trial Sport.
    На этой же странице происходит логин в учетку
    через всплывающее окно.
    Логин - 89131012503
    Пароль - dst_testqa
"""


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    catalog_mountain_ski = '//*[@id="cm3"]/span'
    mountain_ski = '//*[@id="cm3_sub"]/div/div/div/div[1]/div/div[1]/a[3]/p'

    # select_product_2 = "//*[@id='add-to-cart-sauce-labs-bike-light']"
    # select_product_3 = "//*[@id='add-to-cart-sauce-labs-bolt-t-shirt']"
    # cart = "//*[@id='shopping_cart_container']"
    # menu = "//*[@id='react-burger-menu-btn']"
    # link_about = "//*[@id='about_sidebar_link']"

    # Getters

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_mountain_ski)))

    def get_mountain_ski(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mountain_ski)))

    # Actions

    def click_mountain_ski_in_catalog(self):
        self.get_catalog_button().click()
        print("Click mountain ski in catalog")

    def select_mountain_ski(self):
        self.get_mountain_ski().click()
        print("Select mountain ski")

    # Methods

    def mountain_ski_in_catalog(self):
        self.click_mountain_ski_in_catalog()
        time.sleep(1)
        self.select_mountain_ski()
        self.get_current_url()

