"""
Клиент для работы с API Кинопоиска.
"""
import allure
import requests

from config.config import BASE_URL, API_KEY


class KinopoiskApi:
    """Класс для взаимодействия с REST API Кинопоиска."""

    def __init__(
        self,
        base_url: str = BASE_URL,
        api_key: str = API_KEY
    ) -> None:
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            "X-API-Key": self.api_key,
            "Content-Type": "application/json",
        }

    @allure.step("API. Поиск фильма по ключевому слову: {keyword}")
    def search_movie(self, keyword: str, page: int = 1) -> dict:
        url = f"{self.base_url}/api/v2.1/films/search-by-keyword"
        params = {"keyword": keyword, "page": page}
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

    @allure.step("API. Получение карточки фильма по ID: {film_id}")
    def get_movie_by_id(self, film_id: int) -> requests.Response:
        url = f"{self.base_url}/api/v2.2/films/{film_id}"
        response = requests.get(url, headers=self.headers)
        return response

    @allure.step("API. Получение отзывов к фильму по ID: {film_id}")
    def get_reviews(
        self,
        film_id: int,
        page: int = 1,
        count: int = 10
    ) -> requests.Response:
        url = f"{self.base_url}/api/v2.2/films/{film_id}/reviews"
        params = {"page": page, "count": count}
        response = requests.get(
            url, headers=self.headers, params=params
        )
        return response

    @allure.step("API. Поиск фильма с невалидным ключом")
    def search_with_invalid_key(
        self,
        keyword: str
    ) -> requests.Response:
        url = f"{self.base_url}/api/v2.1/films/search-by-keyword"
        params = {"keyword": keyword}
        invalid_headers = {
            "X-API-Key": "invalid_key_123",
            "Content-Type": "application/json",
        }
        response = requests.get(
            url, headers=invalid_headers, params=params
        )
        return response
