"""
Негативный API-тест: невалидный API-ключ.
"""
import allure
import pytest


@allure.epic("Кинопоиск API")
@allure.feature("Обработка ошибок")
@pytest.mark.api
class TestInvalidToken:

    @allure.id("API-4")
    @allure.story("Запрос с невалидным API-ключом")
    @allure.title("Поиск с невалидным ключом возвращает 401")
    @allure.description("Проверяем статус 401 при невалидном ключе")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_with_invalid_key(self, api_client):
        with allure.step("Отправить поиск с невалидным ключом"):
            response = api_client.search_with_invalid_key("Аватар")

        with allure.step("Проверить статус-код 401"):
            assert response.status_code == 401

        with allure.step("Проверить, что тело ответа не пустое"):
            body = response.text
            assert len(body) > 0
            assert "permission" in body.lower()
