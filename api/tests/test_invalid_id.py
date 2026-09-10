"""
Негативный API-тест: невалидный ID фильма.
"""
import allure
import pytest


@allure.epic("Кинопоиск API")
@allure.feature("Обработка ошибок")
@pytest.mark.api
class TestInvalidId:

    @allure.id("API-5")
    @allure.story("Запрос карточки фильма с невалидным ID")
    @allure.title("Получение карточки с ID больше лимита → 400")
    @allure.description("Проверяем статус 400 при ID больше лимита")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_movie_with_invalid_id(self, api_client):
        with allure.step("Отправить запрос с ID 999999999"):
            response = api_client.get_movie_by_id(999999999)

        with allure.step("Проверить статус-код 400"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение об ошибке"):
            data = response.json()
            assert "message" in data
            assert "kinopoisk id should be less than" in data["message"]
