# 🗓️ Django Event Management API

This project is a REST API for event management (conferences, meetups, etc.) with the ability to perform CRUD operations, user registration, authorization, email notifications, API documentation, and launch in Docker.

## Technologies

- Python 3.11
- Django 4.x
- Django REST Framework
- PostgreSQL (через Docker)
- Simple JWT
- drf-yasg (Swagger UI)
- Docker & Docker Compose

## Installation and launch

```bash
# 1. Cloning a repository
git clone <your-repo-url>
cd event_manager

# 2. Running Docker containers
docker-compose up --build

# 3. Migrations and creating a superuser
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# 4. Static file collection
docker-compose exec web python manage.py collectstatic --noinput
```

## Authorization

JWT-токени:

- Getting a token:
  `POST /api/token/`  
  Body: `{ "username": "yourname", "password": "yourpass" }`

- Refresh token:
  `POST /api/token/refresh/`  
  Body: `{ "refresh": "..." }`

## 🔗 API Endpoints

- `GET /api/events/` — list of events
- `POST /api/events/` — create event
- `PUT /api/events/<id>/` — update event
- `DELETE /api/events/<id>/` — delete event
- `POST /api/register/` — user registration
- `POST /api/events/<id>/register/` — event registration
- `POST /api/token/` — get JWT token
- `POST /api/token/refresh/` — refresh JWT token

## 🔍 Accesses

- 🛠️ Admin: [http://localhost:8000/admin](http://localhost:8000/admin)
- 📚 Swagger: [http://localhost:8000/swagger/](http://localhost:8000/swagger/)
- 📦 Events (JSON): [http://localhost:8000/api/events/](http://localhost:8000/api/events/)

## ✉️ Email Notification

After registering for an event, the user receives an email (displayed in the console, because it is used `EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'`).

## 🔎 Search / Filter

Filtering by event name is supported via the query parameter:

```http
GET /api/events/?search=name
```

## Tests

```bash
docker-compose exec web python manage.py test
```

## 📁 Structure

```
├── events/               # events app
├── event_manager/        # main configuration Django
├── templates/emails/     # Email template
├── staticfiles/          # СStatic files
├── .gitignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## 🧩 Options:

- Email sent upon event registration
- Event filtering (search by name)
- Documentation via Swagger
