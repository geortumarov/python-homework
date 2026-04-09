from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_slow_calculator():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    wait = WebDriverWait(driver, 50)

    delay = driver.find_element(By.ID, "delay")
    delay.clear()
    delay.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    result = wait.until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15"))
    assert result

    driver.quit()
