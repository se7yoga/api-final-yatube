# Yatube API

**Yatube API** — это REST API для социальной сети Yatube, созданный на Django REST Framework.

## Описание

Пользователи могут:

- Публиковать посты
- Комментировать посты
- Объединяться в группы
- Подписываться друг на друга

API поддерживает аутентификацию через Token или JWT (Djoser).


## Стек технологий

- Python 3.12+
- Django 4+
- Django REST Framework
- Djoser
- SQLite (по умолчанию)


## Основные эндпоинты

| Endpoint                            | Описание                                    |
| ----------------------------------- | ------------------------------------------- |
| `/api/v1/posts/`                    | Список и создание постов                    |
| `/api/v1/posts/{id}/`               | Получить/обновить/удалить пост              |
| `/api/v1/posts/{post_id}/comments/` | Список и создание комментариев к посту      |
| `/api/v1/groups/`                   | Список всех групп                           |
| `/api/v1/groups/{id}/`              | Информация о группе                         |
| `/api/v1/follow/`                   | Управление подписками пользователя + поиск  |
| `/api/v1/api-token-auth/`           | Получить Token по username и password       |
| `/api/v1/` + Djoser                 | Регистрация, JWT, управление пользователями |


## Аутентификация

- Для большинства POST/DELETE/PUT/PATCH-запросов требуется аутентификация.
- Используется Token или JWT.

Пример:

```http
POST /api/v1/api-token-auth/
{
  "username": "your_username",
  "password": "your_password"
}
```

---

## Примеры запросов

**Создать пост**:

```http
POST /api/v1/posts/
Authorization: Token your_token
Content-Type: application/json

{
  "text": "Новый пост",
  "group": 1
}
```

**Подписаться на пользователя**:

```http
POST /api/v1/follow/
Authorization: Token your_token
Content-Type: application/json

{
  "following": "username"
}
```

**Поиск подписок**:

```http
GET /api/v1/follow/?search=username
Authorization: Token your_token
```

---

## Валидация

- Нельзя подписаться на самого себя — возвращается ошибка.
- Повторная подписка — возвращается ошибка.

---

## Быстрый старт

```bash
# Клонировать репозиторий
git clone https://github.com/yourusername/yourrepo.git
cd yourrepo

# Создать и активировать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows

# Установить зависимости
pip install -r requirements.txt

# Применить миграции
python manage.py migrate

# Запустить сервер
python manage.py runserver
```

---

## Запуск тестов

```bash
pytest
```

---

## Структура

- `views.py` — viewset’ы: Post, Comment, Group, Follow
- `serializers.py` — сериализаторы DRF
- `urls.py` — маршруты DRF и Djoser
- `permissions.py` — кастомные разрешения


## Лицензия

Учебный проект Яндекс.Практикума. Используется только в учебных целях.
