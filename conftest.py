"""
Общие фикстуры для всех тестов проекта.
"""
import pytest
from typing import Generator
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from api.client import KinopoiskApi


@pytest.fixture(scope="session")
def api_client() -> KinopoiskApi:
    """
    Фикстура, создающая экземпляр клиента API Кинопоиска.

    :return: объект KinopoiskApi.
    """
    return KinopoiskApi()


@pytest.fixture
def driver() -> Generator[webdriver.Chrome, None, None]:
    """
    Фикстура для создания и закрытия драйвера Chrome.

    :yield: экземпляр WebDriver Chrome.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()
