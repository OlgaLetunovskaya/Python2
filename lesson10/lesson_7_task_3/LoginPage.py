from selenium.webdriver.common.by import By

class LoginPage:
    """
    Этот класс представляет собой страницу входа на веб-сайт.

    Методы:
    - открыть: Откройте страницу входа в систему.
    - авторизация: Выполните вход в систему, используя стандартные учетные данные.
    """

    def __init__(self, driver):
        """
        Конструктор для класса LoginPage.

        Параметры:
        - драйвер: экземпляр веб-драйвера.

        """
        self.driver = driver

    def open(self):
        """
        Открыть страницу входа в систему
        """
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        """
        Выполнить вход в систему со стандартными учетными данными.
        """
        # Детали реализации