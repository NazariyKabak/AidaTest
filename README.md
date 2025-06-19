# Event Management API

Django REST API для керування подіями: конференціями, мітапами, реєстраціями користувачів та авторизацією через JWT.

---

## Функціонал

- CRUD для подій (назва, опис, дата, місце, організатор)
- Реєстрація на події
- Реєстрація та авторизація користувачів
- JWT-токени
- Swagger-документація
- Docker-підтримка

---

## Швидкий запуск (Docker)

```bash
git clone <repo-url>
cd event_project

# Створення образу та запуск
docker-compose up --build
```

---

## Команди для міграцій

```bash
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate
docker-compose run web python manage.py createsuperuser
```

---

## Тестування API

Документація доступна за адресою:
http://localhost:8000/api/docs/

---

## JWT авторизація

1. Отримати токен:
```
POST /api/token/
```

2. Додати токен у Swagger (Authorize → `Bearer <your_access_token>`)

---

## Ендпоінти

| Метод | URL                          | Опис                       |
|-------|------------------------------|----------------------------|
| POST  | `/api/users/register/`       | Реєстрація користувача     |
| POST  | `/api/token/`                | Отримання токену           |
| GET   | `/api/events/list_events/`   | Список подій               |
| POST  | `/api/events/list_events/`   | Створення події            |
| POST  | `/api/events/registrations/` | Зареєструватись на подію   |
| GET   | `/api/schema/`               | OpenAPI schema (JSON)      |
| GET   | `/api/docs/`                 | Swagger UI                 |

---

## Залежності

- Django
- Django REST Framework
- SimpleJWT
- drf-spectacular
- Docker

---
