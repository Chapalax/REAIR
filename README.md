# Курсовая работа студента группы ИНБО-07-21 Бережного Максима Сергеевича

## Docker

Для запуска приложения в докере:

```bash
docker-compose up
```

Клиентская часть приложения запускается на http://localhost:3000/

## Backend

Для локального запуска сервера необходимо установить poetry

### Установка зависимостей и локальный запуск сервера

```bash
poetry install
poetry run py ./manage.py runserver
```

Сервер запускается на http://localhost:8000/
