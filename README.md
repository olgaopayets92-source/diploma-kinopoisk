# Дипломный проект: автотесты для Кинопоиска

Проект содержит UI- и API-автотесты для сервиса [Кинопоиск](https://www.kinopoisk.ru/) — крупнейшего онлайн-кинотеатра и базы данных фильмов в России.

## 📋 Что тестируется

**UI-функциональность:**
- Поиск фильмов по названию
- Открытие карточки фильма
- Проверка рейтинга и ссылки на рецензии

**API-функциональность:**
- Поиск фильмов по ключевому слову
- Получение карточки фильма по ID
- Получение отзывов к фильму
- Обработка ошибок (невалидный ключ, невалидный ID)

## 🛠️ Стек технологий

- **Python 3.10+**
- **pytest** — фреймворк для тестов
- **Selenium** — UI-автотесты
- **Requests** — API-тесты
- **Allure** — генерация отчётов
- **SQLAlchemy** — работа с БД (используется в доп. задачах)
- **python-dotenv** — переменные окружения

## 📁 Структура проекта
diploma-kinopoisk/
├── api/ # API-тесты
│ ├── client.py # Клиент KinopoiskApi
│ └── tests/ # 7 API-тестов
├── ui/ # UI-тесты
│ ├── pages/ # Page Object классы
│ │ ├── main_page.py
│ │ ├── search_page.py
│ │ └── movie_page.py
│ └── tests/ # 7 UI-тестов
├── config/ # Конфигурация
│ └── config.py # Чтение .env
├── conftest.py # Фикстуры pytest
├── pytest.ini # Маркеры и настройки
├── requirements.txt # Зависимости
├── .env.example # Пример переменных окружения
├── .gitignore
└── README.md

## ⚙️ Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/olgaopayets92-source/diploma-kinopoisk.git
   cd diploma-kinopoisk

Создайте виртуальное окружение:

python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux
Установите зависимости:

pip install -r requirements.txt
Создайте файл .env в корне проекта и укажите в нём API-ключ:

BASE_URL=https://kinopoiskapiunofficial.tech
API_KEY=ваш_ключ_из_личного_кабинета
API-ключ можно получить бесплатно на kinopoiskapiunofficial.tech.

🚀 Запуск тестов
Все тесты

pytest
Только UI-тесты

pytest -m "ui"
Только API-тесты

pytest -m "api"
С генерацией результатов для Allure

pytest --alluredir=allure-results
📊 Allure-отчёты
Просмотр отчёта

allure serve allure-results
Если команда allure не распознаётся (Windows, установка через Scoop):

C:\Users\%USERNAME%\scoop\apps\allure\current\bin\allure.bat serve allure-results
Генерация статического отчёта

allure generate allure-results -o allure-report --clean
allure open allure-report
🔧 Установка Allure (Windows)
Установите Scoop (если ещё не установлен):

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Invoke-RestMethod -Uri https://get.scoop.sh | Invoke-Expression
Установите Allure:

scoop install allure
📝 Документация тестов
Все тесты содержат:

Allure-разметку: @allure.epic, @allure.feature, @allure.story, @allure.title, @allure.description, @allure.severity

Allure-шаги: with allure.step("...")

Docstrings и аннотации типов для методов

Соблюдение PEP8

📌 Ссылки
Страница проекта в Yonote: https://olgaopayets92.yonote.ru/share/78f7595a-958f-4c71-afb4-9e16051242b7
Документация API: https://kinopoiskapiunofficial.tech/documentation/api/

📄 Лицензия
Учебный проект, создан в рамках курса SkyPro.