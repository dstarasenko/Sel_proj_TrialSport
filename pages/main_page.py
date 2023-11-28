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

class Main_page(Base):

    main_url = "https://trial-sport.ru/"


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    profile_button = "//*[@id='asc']/div[1]/div/div[2]/div/span/span"
    user_name = "//*[@id='idLogForm']/table/tbody/tr/td[1]/table/tbody/tr[1]/td[2]/div/input"
    password = "//*[@id='idLogForm']/table/tbody/tr/td[1]/table/tbody/tr[3]/td[2]/div/input"
    login_button = "//*[@id='idLogForm']/table/tbody/tr/td[1]/table/tbody/tr[5]/td[2]/div/div/input"

    #Getters

    def get_profile_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.profile_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))


    # Actions

    def click_profile_button(self):
        self.get_profile_button().click()
        print("Click profile button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name ")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")


    #Methods

    def authorization(self):
        self.driver.get(self.main_url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_profile_button()
        self.input_user_name("89131012503")
        self.input_password("dst_testqa")
        self.click_login_button()


