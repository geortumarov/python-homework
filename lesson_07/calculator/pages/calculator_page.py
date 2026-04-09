from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 50)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html")

    def set_delay(self, seconds: str):
        delay_input = self.driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys(seconds)

    def click_button(self, text: str):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{text}']").click()

    def wait_for_result(self, expected: str):
        self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), expected))

    def get_result_text(self) -> str:
        return self.driver.find_element(
            By.CLASS_NAME, "screen").text
