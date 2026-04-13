from selenium.webdriver.common.by import By


class LoginPage:
    """Page Object для страницы авторизации SauceDemo."""
    def __init__(self, driver):
        """
        Инициализация страницы авторизации.
        Args:
            driver: WebDriver instance
        """
        self.driver = driver

    def open(self) -> None:
        """Открывает страницу авторизации в браузере."""
        self.driver.get(
            "https://www.saucedemo.com/")

    def login(self, username: str, password: str) -> None:
        """
        Выполняет авторизацию с указанными учётными данными.
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.driver.find_element(
            By.ID, "user-name").send_keys(username)
        self.driver.find_element(
            By.ID, "password").send_keys(password)
        self.driver.find_element(
            By.ID, "login-button").click()
