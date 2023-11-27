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


class Mountain_ski_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    f_price_from = '//*[@id="filter_form"]/div[1]/div[3]/div[2]/div/table/tbody/tr/td[1]/div/input'
    f_price_to = '//*[@id="filter_form"]/div[1]/div[3]/div[2]/div/table/tbody/tr/td[3]/div/input'
    brand_button = '//*[@id="filter_form"]/div[1]/div[3]/div[4]/h4'
    f_brand = '//*[@id="filter_form"]/div[1]/div[3]/div[4]/div[5]/label'
    age_button = '//*[@id="filter_form"]/div[1]/div[3]/div[6]/h4'
    f_age = '//*[@id="filter_form"]/div[1]/div[3]/div[6]/div[1]/label'
    level_button = '//*[@id="filter_form"]/div[1]/div[3]/div[9]/h4'
    f_level = '//*[@id="filter_form"]/div[1]/div[3]/div[9]/div[3]/label'
    #reset_button = '//*[@id="filter_form"]/div[1]/div[3]/div[13]/div/input'

    # Getters

    def get_f_price_from(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_price_from)))

    def get_f_price_to(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_price_to)))

    def get_brand_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.brand_button)))

    def get_f_brand(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_brand)))

    def get_age_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.age_button)))

    def get_f_age(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_age)))

    def get_level_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.level_button)))

    def get_f_level(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.f_level)))


    # Actions

    def input_price_from(self, price_from):
        self.get_f_price_from().send_keys(price_from)
        print(f"Input price from {price_from}")

    def input_price_to(self, price_to):
        self.get_f_price_to().send_keys(price_to)
        print(f"Input price from {price_to}")

    def click_brand_button(self):
        self.get_brand_button().click()
        print(f"Click brand button")

    def select_brand(self):
        self.get_f_brand().click()
        print(f"Select brand Rossignol")

    def click_age_button(self):
        self.get_age_button().click()
        print(f"Click age button")

    def select_age(self):
        self.get_f_age().click()
        print(f"Select age for adults")

    def click_level_button(self):
        self.get_level_button().click()
        print(f"Click level button")

    def select_level(self):
        self.get_f_level().click()
        print(f"Select level expert")


    # Methods

    def mountain_ski_filters(self):
        self.input_price_from("70000")
        self.input_price_to("80000")
        self.click_brand_button()
        self.select_brand()
        self.click_age_button()
        self.select_age()
        self.click_level_button()
        self.select_level()
        self.driver.execute_script('window.scrollTo(0,600)')




