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


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_town_field = '//*[@id="frm"]/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/input[1]'
    select_tomsk_button = '//*[@id="frm"]/div/div[3]/table/tbody/tr[1]/td[3]/div[2]/div/span[1]'
    checkout_button = '//*[@id="frm"]/div/div[3]/table/tbody/tr[3]/td[5]/div/div/input'



    # Getters

    def get_select_town_field(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_town_field)))

    def get_select_tomsk_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_tomsk_button)))

    def get_checkout_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout_button)))


    # Actions

    def input_select_town_field(self, text):
        self.get_select_town_field().send_keys(text)
        print(f"Enter town 'Томск' into the delivery city field ")

    def click_select_tomsk_button(self):
        self.get_select_tomsk_button().click()
        print(f"Select 'Томск, Томская обл.' in the delivery city field")

    def click_checkout_button(self):
        self.get_checkout_button().click()
        print(f"Click checkout button")


    # Methods

    def checkout(self):
        self.get_current_url()
        self.input_select_town_field("Томск")
        self.click_select_tomsk_button()
        self.click_checkout_button()




