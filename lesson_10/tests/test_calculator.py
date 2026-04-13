import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@allure.title("Тест медленного калькулятора")
@allure.description("Проверка работы калькулятора с задержкой 45 секунд")
@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
def test_slow_calculator():
    with allure.step("Инициализация драйвера Chrome"):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
    try:
        page = CalculatorPage(driver)
        with allure.step("Открытие страницы калькулятора"):
            page.open()
        with allure.step("Установка задержки: 45 секунд"):
            page.set_delay("45")
        with allure.step("Выполнение вычисления: 7 + 8"):
            page.click_button("7")
            page.click_button("+")
            page.click_button("8")
            page.click_button("=")
        with allure.step("Ожидание результата 15"):
            page.wait_for_result("15")
        with allure.step("Проверка результата"):
            result = page.get_result_text()
            assert result == "15", f"Ожидалось 15, получено {result}"
    finally:
        with allure.step("Закрытие браузера"):
            driver.quit()
