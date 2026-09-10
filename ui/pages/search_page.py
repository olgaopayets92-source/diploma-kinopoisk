"""
Page Object для страницы результатов поиска Кинопоиска.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SearchPage:
    """Класс для работы со страницей результатов поиска."""

    FIRST_MOVIE_LINK = (
        By.CSS_SELECTOR,
        "div[data-test-id='movie-list-item'] a[href*='/film/']"
    )

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Проверить, что открылась страница результатов поиска")
    def is_opened(self) -> bool:
        try:
            self.wait.until(
                EC.presence_of_element_located(self.FIRST_MOVIE_LINK)
            )
            return True
        except Exception:
            return False

    @allure.step("Открыть карточку первого фильма из результатов")
    def open_first_movie(self) -> "SearchPage":
        first_movie = self.wait.until(
            EC.element_to_be_clickable(self.FIRST_MOVIE_LINK)
        )
        first_movie.click()
        # Ждём, пока URL изменится на страницу фильма
        self.wait.until(EC.url_contains("/film/"))
        return self
