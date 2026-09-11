"""
Page Object для главной страницы Кинопоиска.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    """Класс для работы с главной страницей Кинопоиска."""

    SEARCH_INPUT = (By.CSS_SELECTOR, "input[name='text']")
    URL = "https://www.kinopoisk.ru/"

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Открыть главную страницу Кинопоиска")
    def open(self) -> "MainPage":
        self.driver.get(self.URL)
        return self

    @allure.step("Закрыть всплывающее модальное окно")
    def close_modal(self) -> "MainPage":
        """
        Удаляет модальное окно (реклама, куки и т.п.) через JavaScript.

        Использует WebDriverWait вместо time.sleep для стабильности.

        :return: текущий экземпляр страницы.
        """
        # Ждём появления модального окна (или истечения таймаута)
        WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".ReactModal__Overlay")
            )
        )
        # Удаляем модальные окна
        self.driver.execute_script(
            "document.querySelectorAll('.ReactModal__Overlay')"
            ".forEach(el => el.remove());"
            "document.querySelectorAll('.ReactModal__Content')"
            ".forEach(el => el.remove());"
            "document.body.style.overflow = 'auto';"
        )
        return self

    @allure.step("Найти фильм по названию: {keyword}")
    def search_movie(self, keyword: str) -> "MainPage":
        search_input = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_INPUT)
        )
        search_input.clear()
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)
        self.wait.until(EC.url_contains("text="))
        return self
