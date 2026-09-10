"""
API-тесты для карточки фильма.
"""
import allure
import pytest


@allure.epic("Кинопоиск API")
@allure.feature("Карточка фильма")
@pytest.mark.api
class TestMovieCard:

    @allure.id("API-2")
    @allure.story("Получение карточки фильма по ID")
    @allure.title("Карточка фильма 'Аватар' содержит нужные поля")
    @allure.description("Проверяем полную информацию карточки")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_get_movie_card(self, api_client):
        with allure.step("Отправить запрос с ID 251733"):
            response = api_client.get_movie_by_id(251733)

        with allure.step("Проверить статус-код 200"):
            assert response.status_code == 200

        with allure.step("Проверить поля карточки фильма"):
            data = response.json()
            assert data["kinopoiskId"] == 251733
            assert data["nameRu"] == "Аватар"
            assert data["nameOriginal"] == "Avatar"
            assert data["year"] == 2009
            assert data["ratingKinopoisk"] == 8.0
            assert data["description"] != ""
            assert data["posterUrl"].startswith("https://")
