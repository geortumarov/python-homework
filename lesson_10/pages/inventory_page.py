from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage:
    """Page Object для страницы каталога товаров SauceDemo."""
    def __init__(self, driver):
        """
        Инициализация страницы каталога.
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_id: str) -> None:
        """
        Добавляет товар в корзину по его ID.
        Args:
            item_id: ID кнопки добавления товара
        """
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.ID, item_id)))
        button.click()

    def go_to_cart(self) -> None:
        """Переходит в корзину покупок."""
        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
