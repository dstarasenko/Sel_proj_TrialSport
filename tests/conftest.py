import pytest


@pytest.fixture()
def set_up():  # Добавить этот метод в аргументы теста
    print("Start Test")
    # driver = webdriver.Chrome()
    # url = "https://www.saucedemo.com/"
    # self.driver.get(self.url)
    # self.driver.maximize_window()

    yield

    # driver.quit()
    print("Finish Test")


@pytest.fixture(scope="module")  # Для всего файла
def set_group():
    print("Enter system")
    yield
    print("Exit System")
