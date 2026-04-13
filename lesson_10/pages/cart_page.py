from selenium.webdriver.common.by import By


class CartPage:
    """Page Object для страницы корзины SauceDemo."""
    def __init__(self, driver):
        """
        Инициализация страницы корзины.
        Args:
            driver: WebDriver instance
        """
        self.driver = driver

    def click_checkout(self) -> None:
        """Нажимает кнопку оформления заказа."""
        self.driver.find_element(
            By.ID, "checkout").click()
