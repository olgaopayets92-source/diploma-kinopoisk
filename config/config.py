"""
Модуль конфигурации проекта.

Загружает переменные окружения из .env и предоставляет
доступ к базовому URL и API-ключу.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL: str = os.getenv("BASE_URL", "https://kinopoiskapiunofficial.tech")
API_KEY: str = os.getenv("API_KEY", "")

if not API_KEY:
    raise ValueError(
        "API_KEY не найден. Создайте файл .env и укажите в нём API_KEY."
    )
