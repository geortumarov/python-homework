from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
driver = webdriver.Firefox(
    service=FirefoxService(GeckoDriverManager().install())
)
driver.maximize_window()
driver.get("http://the-internet.herokuapp.com/login")
search_user_name = driver.find_element(By.CSS_SELECTOR, '#username')
search_user_name.send_keys('tomsmith')
sleep(2)
search_password = driver.find_element(By.CSS_SELECTOR, '#password')
search_password.send_keys('SuperSecretPassword!')
sleep(2)
bottom_push_login = driver.find_element(By.CLASS_NAME, "radius")
bottom_push_login.click()
sleep(2)
green_alert = driver.find_element(By.ID, "flash").text
print(green_alert)
driver.quit()
