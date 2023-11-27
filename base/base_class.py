import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """ Получение текущей URL """
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")


    """ Метод проверки наличия слова на странице """
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")


    """ Создание скриншота """
    def get_screenshot(self):
        now_date = datetime.datetime.now(datetime.UTC).strftime("%Y.%m.%d.%H.%M.%S")
        self.driver.save_screenshot(f"C:\\Users\\dstar\\PycharmProjects\\main_project\\screen\\finish_{now_date}.png")


    """ Метод проверки URL """
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")

