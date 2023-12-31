# Notes Manager

Проект "Notes Manager" является простым веб-приложением, 
которое позволяет пользователям выполнять CRUD операции 
(Создание, Чтение, Обновление, Удаление) с заметками в базе данных.
В проекте реализована интеграция с внешним API для получения свежих новостей в сфере IT.

## Основные возможности:

- **Управление заметками:** Создание, редактирование и удаление заметок.
- **Регистрация, аутентификация и авторизация пользователей:**
- **Просмотр списка свежих новостей в сфере IT**

## Технологии:

- **Django:** Фреймворк для создания веб-приложений на Python. Используется для управления бэкенд-логикой, 
базой данных PostgreSQL, URL-ми, аутентификацией и шаблонами.
- **PostgreSQL:** Реляционная база данных для хранения информации о сотрудниках и задачах.
- **aiohttp:** Фреймворк для создания веб-серверов и клиентов с поддержкой асинхронности в Python.
- **Redis:** Высокопроизводительная система управления данными, используемая как кэш, база данных и брокер сообщений. 
В проекте используется для кэширования часто используемых запросов и ускорения доступа к данным.
- **Unittest:** Встроенный модуль в Python для создания и запуска тестов.

Таким образом, проект включает в себя современные инструменты для разработки, тестирования и управления базой данных, 
что обеспечивает надежность, масштабируемость и легкость сопровождения.

## Установка и запуск локально:

- Клонируйте репозиторий на вашем компьютере:
```bash
git clone - git clone https://github.com/Lisnevskiy/NotesManagerDjango.git
```
- Установите зависимости:
```bash
pip install -r requirements.txt
```

- Создайте базу данных PostgreSQL либо используйте уже существующую.

- Создайте файл .env в корневой директории проекта и укажите в нем необходимые переменные окружения, 
пример которых указан в файле [.env.sample](.env.sample). 
Убедитесь, что значения переменных окружения соответствуют вашей конфигурации.

- Выполните миграции базы данных командой:
```bash
python manage.py migrate
```

- Запустите приложение командой:
```bash
python manage.py runserver
```

- Для запуска тестов:
```bash
python manage.py test
```

## Эндпоинты:
- **CRUD для заметок** - /notes/...
- **Получение новостей** - /notes/news/
- **Регистрация, авторизация пользователя** - /users/register/; /users/login/
- **Выход пользователя из системы.** - /users/logout/
