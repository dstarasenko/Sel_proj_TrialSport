import time

from selenium.webdriver import ActionChains
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


class Product_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_product_button = '//*[@id="obj2178608"]/span[2]/a[1]/span/font'
    add_to_cart_button = '/html/body/div[4]/div[3]/div[6]/div[1]/div[2]/div[3]/div[1]/a[1]'
    add_to_cart_repeat_button = '/html/body/div[4]/div[6]/div[11]/div[2]/div[2]/form/table[2]/tbody/tr/td[3]/div/div/input'
    go_to_cart_button = '/html/body/div[4]/div[9]/div[5]/div[2]/div[3]/div[2]/div[2]/div[2]/a[2]'


    # Getters

    def get_select_product_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_button)))

    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_add_to_cart_repeat_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_repeat_button)))

    def get_go_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart_button)))



    # Actions

    def click_select_product_button(self):
        self.get_select_product_button().click()
        print(f"Click select product button")

    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print(f"Click add to cart button")

    def click_add_to_cart_repeat_button(self):
        self.get_add_to_cart_repeat_button().click()
        print(f"Click add to cart repeat button")

    def click_go_to_cart_button(self):
        self.get_go_to_cart_button().click()
        print(f"Click go to cart button")


    # Methods

    def add_product_to_cart(self):
        self.get_current_url()
        self.click_select_product_button()
        self.click_add_to_cart_button()
        self.click_add_to_cart_repeat_button()
        self.click_go_to_cart_button()




