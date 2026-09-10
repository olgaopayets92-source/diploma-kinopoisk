"""
Page Object для страницы карточки фильма на Кинопоиске.
"""
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MoviePage:
    """Класс для работы со страницей карточки фильма."""

    MOVIE_TITLE = (By.CSS_SELECTOR, "span[data-tid='75209b22']")
    RATING = (By.CSS_SELECTOR, "span[data-tid='939058a8']")
    REVIEWS_LINK = (By.CSS_SELECTOR, "a[href*='/reviews/']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    @allure.step("Получить название фильма")
    def get_title(self) -> str:
        """Получить название фильма со страницы."""
        title = self.wait.until(
            EC.visibility_of_element_located(self.MOVIE_TITLE)
        )
        return title.text

    @allure.step("Проверить, что карточка фильма открылась")
    def is_opened(self) -> bool:
        """Проверить, что карточка фильма загружена."""
        try:
            self.wait.until(EC.presence_of_element_located(self.MOVIE_TITLE))
            return True
        except Exception:
            return False

    @allure.step("Получить рейтинг фильма")
    def get_rating(self) -> str:
        """Получить рейтинг фильма (например, '8.0')."""
        rating = self.wait.until(
            EC.presence_of_element_located(self.RATING)
        )
        return rating.text

    @allure.step("Проверить, что есть ссылка на рецензии")
    def is_reviews_link_displayed(self) -> bool:
        """Проверить, есть ли ссылка на рецензии."""
        try:
            self.wait.until(EC.presence_of_element_located(self.REVIEWS_LINK))
            return True
        except Exception:
            return False
