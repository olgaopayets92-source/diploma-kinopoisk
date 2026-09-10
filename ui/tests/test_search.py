"""
UI-тесты для Кинопоиска.
"""
import os
import allure
import pytest

from ui.pages.main_page import MainPage
from ui.pages.search_page import SearchPage
from ui.pages.movie_page import MoviePage


@allure.epic("Кинопоиск UI")
@allure.feature("Поиск фильмов")
@pytest.mark.ui
class TestSearchMovie:

    @allure.id("UI-1")
    @allure.story("Поиск фильма по названию")
    @allure.title("Поиск 'Аватар' и открытие карточки")
    @allure.description("Проверяем поиск и открытие карточки фильма")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_movie(self, driver):
        os.makedirs("screenshots", exist_ok=True)

        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()

        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()

        with allure.step("Ввести 'Аватар' в поиск"):
            main_page.search_movie("Аватар")

        with allure.step("Проверить страницу результатов"):
            search_page = SearchPage(driver)
            assert search_page.is_opened(), "Результаты не загрузились"

        with allure.step("Открыть первый фильм"):
            search_page.open_first_movie()

        with allure.step("Проверить карточку фильма 'Аватар'"):
            movie_page = MoviePage(driver)
            assert movie_page.is_opened(), "Карточка не загрузилась"
            title = movie_page.get_title()
            assert "Аватар" in title, f"Нет 'Аватар': {title}"

    @allure.id("UI-2")
    @allure.story("Открытие карточки по прямой ссылке")
    @allure.title("Открытие карточки 'Аватар' по ID 251733")
    @allure.description("Переход по прямой ссылке")
    @allure.severity(allure.severity_level.NORMAL)
    def test_open_movie_by_direct_url(self, driver):
        with allure.step("Открыть карточку фильма"):
            driver.get("https://www.kinopoisk.ru/film/251733/")

        with allure.step("Проверить заголовок"):
            movie_page = MoviePage(driver)
            assert movie_page.is_opened()
            title = movie_page.get_title()
            assert "Аватар" in title, f"Нет 'Аватар': {title}"

    @allure.id("UI-3")
    @allure.story("Проверка рейтинга фильма")
    @allure.title("На карточке 'Аватар' отображается рейтинг")
    @allure.description("Проверяем наличие рейтинга")
    @allure.severity(allure.severity_level.NORMAL)
    def test_movie_rating_displayed(self, driver):
        with allure.step("Открыть карточку фильма"):
            driver.get("https://www.kinopoisk.ru/film/251733/")

        with allure.step("Проверить рейтинг"):
            movie_page = MoviePage(driver)
            rating = movie_page.get_rating()
            assert rating != "", "Рейтинг пустой"

    @allure.id("UI-4")
    @allure.story("Поиск другого фильма")
    @allure.title("Поиск 'Титаник' и открытие карточки")
    @allure.description("Проверяем, что поиск работает для любого фильма")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_another_movie(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()

        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()

        with allure.step("Ввести 'Титаник'"):
            main_page.search_movie("Титаник")

        with allure.step("Проверить результаты"):
            search_page = SearchPage(driver)
            assert search_page.is_opened()

        with allure.step("Открыть первый фильм"):
            search_page.open_first_movie()

        with allure.step("Проверить заголовок 'Титаник'"):
            movie_page = MoviePage(driver)
            title = movie_page.get_title()
            assert "Титаник" in title, f"Нет 'Титаник': {title}"

    @allure.id("UI-5")
    @allure.story("Проверка ссылки на рецензии")
    @allure.title("На карточке 'Аватар' есть ссылка на рецензии")
    @allure.description("Проверяем ссылку на рецензии")
    @allure.severity(allure.severity_level.MINOR)
    def test_movie_reviews_link(self, driver):
        with allure.step("Открыть карточку фильма"):
            driver.get("https://www.kinopoisk.ru/film/251733/")

        with allure.step("Проверить ссылку на рецензии"):
            movie_page = MoviePage(driver)
            assert movie_page.is_reviews_link_displayed()

    @allure.id("UI-6")
    @allure.story("Заголовок карточки содержит год")
    @allure.title("Заголовок 'Аватар' содержит год выпуска")
    @allure.description("Проверяем формат заголовка с годом")
    @allure.severity(allure.severity_level.MINOR)
    def test_movie_title_contains_year(self, driver):
        with allure.step("Открыть карточку фильма"):
            driver.get("https://www.kinopoisk.ru/film/251733/")

        with allure.step("Проверить, что заголовок содержит год"):
            movie_page = MoviePage(driver)
            title = movie_page.get_title()
            assert "Аватар" in title, f"Нет 'Аватар': {title}"
            assert "2009" in title, f"Нет года: {title}"

    @allure.id("UI-7")
    @allure.story("Поиск несуществующего фильма")
    @allure.title("Поиск по вымышленному запросу не даёт результатов")
    @allure.description("Проверяем поиск случайного текста")
    @allure.severity(allure.severity_level.MINOR)
    def test_search_nonexistent_movie(self, driver):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(driver)
            main_page.open()

        with allure.step("Закрыть модальное окно"):
            main_page.close_modal()

        with allure.step("Ввести вымышленный запрос"):
            main_page.search_movie("ксщываорлджщшгнекуцй")

        with allure.step("Проверить отсутствие результатов"):
            search_page = SearchPage(driver)
            assert not search_page.is_opened(), "Найдены результаты"
