from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


def test_slow_calculator():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    page = CalculatorPage(driver)
    page.open()
    page.set_delay("45")
    page.click_button("7")
    page.click_button("+")
    page.click_button("8")
    page.click_button("=")
    page.wait_for_result("15")
    assert page.get_result_text() == "15"

    driver.quit()
