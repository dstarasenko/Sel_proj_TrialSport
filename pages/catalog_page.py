import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base

""" 
    Главная страница магазина.
    Делаем клик по пункту "Лыжи горные" в левом меню каталога.
    Далее клик по пункту "Лыжи горные" во всплывающем окне
    для перехода к фильтрам.
"""


class Catalog_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Локаторы

    catalog_mountain_ski = '//*[@id="cm3"]/span'  # Локатор пункта "Лыжи горные" в левом меню каталога
    mountain_ski = '//*[@id="cm3_sub"]/div/div/div/div[1]/div/div[1]/a[3]/p' # Локатор пункта "Лыжи горные" во всплывающем окне для перехода к фильтрам.

    # Геттеры

    def get_catalog_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.catalog_mountain_ski)))

    def get_mountain_ski(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.mountain_ski)))

    # Действия

    def click_mountain_ski_in_catalog(self):
        self.get_catalog_button().click()
        print("Click mountain ski in left catalog")

    def select_mountain_ski(self):
        self.get_mountain_ski().click()
        print("Select mountain ski in a pop-up window")

    # Методы

    def mountain_ski_in_catalog(self):
        self.get_current_url()
        self.click_mountain_ski_in_catalog()
        self.select_mountain_ski()


