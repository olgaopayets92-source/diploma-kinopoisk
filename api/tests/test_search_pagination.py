"""
API-тесты для пагинации и пустого поиска.
"""
import allure
import pytest


@allure.epic("Кинопоиск API")
@allure.feature("Поиск фильмов")
@pytest.mark.api
class TestSearchPagination:

    @allure.id("API-6")
    @allure.story("Пагинация результатов поиска")
    @allure.title("Поиск 'Аватар' возвращает несколько страниц")
    @allure.description("Проверяем, что pagesCount >= 2")
    @allure.severity(allure.severity_level.NORMAL)
    def test_search_pagination(self, api_client):
        with allure.step("Отправить поиск 'Аватар' с page=2"):
            response = api_client.search_movie("Аватар", page=2)

        with allure.step("Проверить статус-код 200"):
            assert response.status_code == 200

        with allure.step("Проверить, что есть поле films"):
            data = response.json()
            assert "films" in data
            assert isinstance(data["films"], list)

        with allure.step("Проверить пагинацию"):
            assert "pagesCount" in data
            assert data["pagesCount"] >= 2

    @allure.id("API-7")
    @allure.story("Поиск с пустым ключевым словом")
    @allure.title("Поиск с пустым keyword возвращает пусто или ошибку")
    @allure.description("Проверяем реакцию API на пустой запрос")
    @allure.severity(allure.severity_level.MINOR)
    def test_search_with_empty_keyword(self, api_client):
        with allure.step("Отправить поиск с пустым keyword"):
            response = api_client.search_movie("")

        with allure.step("Проверить, что API обработал запрос"):
            # API может вернуть 200 с пустым списком или ошибку
            assert response.status_code in [200, 400, 422]

        if response.status_code == 200:
            with allure.step("Проверить, что фильмов нет"):
                data = response.json()
                assert "films" in data
                assert len(data["films"]) == 0
