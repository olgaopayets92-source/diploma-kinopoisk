"""
API-тесты для отзывов к фильму.
"""
import allure
import pytest


@allure.epic("Кинопоиск API")
@allure.feature("Отзывы к фильму")
@pytest.mark.api
class TestReviews:

    @allure.id("API-3")
    @allure.story("Получение отзывов к фильму по ID")
    @allure.title("Отзывы к фильму 'Аватар' содержат данные")
    @allure.description("Проверяем статистику и список отзывов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_reviews(self, api_client):
        with allure.step("Отправить запрос на отзывы ID 251733"):
            response = api_client.get_reviews(251733, page=1, count=10)

        with allure.step("Проверить статус-код 200"):
            assert response.status_code == 200

        with allure.step("Проверить статистику отзывов"):
            data = response.json()
            assert "total" in data
            assert data["total"] > 0
            assert "totalPages" in data
            assert "totalPositiveReviews" in data
            assert "totalNegativeReviews" in data
            assert "totalNeutralReviews" in data

        with allure.step("Проверить, что есть массив отзывов items"):
            assert "items" in data
            assert len(data["items"]) > 0

        with allure.step("Проверить поля первого отзыва"):
            first_review = data["items"][0]
            assert "author" in first_review
            assert "date" in first_review
            assert "description" in first_review
            assert "type" in first_review
