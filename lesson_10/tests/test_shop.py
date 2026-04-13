import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.title("Тест оформления заказа в интернет-магазине")
@allure.description("Проверка итоговой суммы заказа из трёх товаров")
@allure.feature("Магазин")
@allure.severity(allure.severity_level.BLOCKER)
def test_shop_total_price():
    with allure.step("Инициализация драйвера Firefox"):
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    try:
        with allure.step("Авторизация в магазине"):
            login_page = LoginPage(driver)
            login_page.open()
            login_page.login("standard_user", "secret_sauce")
        with allure.step("Добавление товаров в корзину"):
            inventory = InventoryPage(driver)
            inventory.add_to_cart("add-to-cart-sauce-labs-backpack")
            inventory.add_to_cart("add-to-cart-sauce-labs-bolt-t-shirt")
            inventory.add_to_cart("add-to-cart-sauce-labs-onesie")
        with allure.step("Переход в корзину"):
            inventory.go_to_cart()
        with allure.step("Переход к оформлению заказа"):
            cart = CartPage(driver)
            cart.click_checkout()
        with allure.step("Заполнение формы оплаты"):
            checkout = CheckoutPage(driver)
            checkout.fill_form("Георгий", "Тумаров", "123456")
        with allure.step("Получение итоговой суммы"):
            total = checkout.get_total()
        with allure.step("Проверка итоговой суммы"):
            assert total == "Total: $58.29", (
                f"Ожидалось Total: $58.29, получено {total}"
            )
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
