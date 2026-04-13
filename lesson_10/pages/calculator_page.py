from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """Page Object для страницы медленного калькулятора."""
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.
        Args:
            driver: WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self) -> None:
        """Открывает страницу калькулятора в браузере."""
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, seconds: str) -> None:
        """
        Устанавливает задержку выполнения операций.
        Args:
            seconds: Значение задержки в секундах (как строка)
        """
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text: str) -> None:
        """
        Нажимает кнопку калькулятора с указанным текстом.
        Args:
            text: Текст на кнопке (цифра или оператор)
        """
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']").click()

    def wait_for_result(self, expected: str) -> None:
        """
        Ожидает появления ожидаемого результата на экране.
        Args:
            expected: Ожидаемое значение
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected))

    def get_result_text(self) -> str:
        """
        Получает текущее значение на экране калькулятора.
        Returns:
            Текст, отображаемый на экране
        """
        return self.driver.find_element(
            By.CLASS_NAME, "screen").text
