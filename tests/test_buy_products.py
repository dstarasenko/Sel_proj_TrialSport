import time
from selenium import webdriver

from pages.catalog_page import Catalog_page
from pages.main_page import Main_page
from pages.mountain_ski_filters_page import Mountain_ski_filters_page
from pages.product_page import Product_page
from pages.cart_page import Cart_page
from pages.delivery_page import Delivery_page


def test_select_products():
    driver = webdriver.Chrome()

    # Авторизация на сайте
    mp = Main_page(driver)
    mp.authorization()
    time.sleep(1)

    # Переходим в каталог, выбираем раздел "горные лыжи"
    cat_p = Catalog_page(driver)
    cat_p.mountain_ski_in_catalog()
    time.sleep(1)

    # Активируем фильтры
    msp = Mountain_ski_filters_page(driver)
    msp.mountain_ski_filters()
    time.sleep(1)

    # Выбираем лыжи, добавляем в корзину
    pp = Product_page(driver)
    pp.add_product_to_cart()
    time.sleep(1)

    # Начало оформления заказа: выбираем город доставки и кликаем "оформить"
    cp = Cart_page(driver)
    cp.checkout()
    time.sleep(1)

    # Заполнение данных получателя заказа
    dp = Delivery_page(driver)
    dp.entering_delivery_data()
    time.sleep(1)

    time.sleep(5)