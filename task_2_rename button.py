from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)
driver.maximize_window()
driver.get('http://uitestingplayground.com/textinput')
input = driver.find_element(By.CSS_SELECTOR, '#newButtonName')
input.clear()
input.send_keys('skypro')
button = driver.find_element(By.CSS_SELECTOR, '#updatingButton')
button.click()
wait = WebDriverWait(driver, 4)
wait.until(
    EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, '#updatingButton'), 'skypro'))
print(button.text)
driver.quit()
