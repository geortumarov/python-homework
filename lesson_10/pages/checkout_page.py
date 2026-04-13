from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Page Object для страницы оформления заказа SauceDemo."""
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self,
                  first_name: str,
                  last_name: str,
                  postal_code: str) -> None:
        """
        Заполняет форму оплаты и переходит к следующему шагу.
        Args:
            first_name: Имя
            last_name: Фамилия
            postal_code: Почтовый индекс
        """
        self.driver.find_element(
            By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(
            By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(
            By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(
            By.ID, "continue").click()

    def get_total(self) -> str:
        """
        Получает итоговую сумму заказа.
        Returns:
            Текст с итоговой суммой
        """
        total_element = self.wait.until(
            EC.presence_of_element_located(
                (By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text
