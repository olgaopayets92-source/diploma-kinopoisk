"""
API-тесты для поиска фильмов.
"""
import allure
import pytest


@allure.epic("Кинопоиск API")
@allure.feature("Поиск фильмов")
@pytest.mark.api
class TestSearchMovie:

    @allure.id("API-1")
    @allure.story("Поиск фильма по ключевому слову")
    @allure.title("Поиск 'Аватар' возвращает корректные данные")
    @allure.description("Проверяем поля первого фильма в ответе")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_search_movie_by_keyword(self, api_client):
        with allure.step("Отправить запрос на поиск 'Аватар'"):
            response = api_client.search_movie("Аватар")

        with allure.step("Проверить статус-код 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что в ответе есть фильмы"):
            data = response.json()
            assert "films" in data
            assert len(data["films"]) > 0

        with allure.step("Проверить данные первого фильма"):
            first_film = data["films"][0]
            assert first_film["filmId"] == 251733
            assert first_film["nameRu"] == "Аватар"
            assert first_film["nameEn"] == "Avatar"
            assert first_film["year"] == "2009"
            assert first_film["rating"] == "8.0"
