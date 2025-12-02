# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Django starter application built following the official Django tutorial. It's a learning project demonstrating Django framework fundamentals with a PostgreSQL database backend. The project contains two Django apps: `polls` (a voting application) and `dash` (a dashboard/landing page).

## Architecture

### Multi-App Structure

The project follows Django's multi-app architecture pattern:
- **mysite/**: Django project root containing settings and main URL routing
- **polls/**: Voting application with Question/Choice models
- **dash/**: Dashboard app serving as the landing page at root URL

### URL Routing Hierarchy

URL routing flows from [mysite/mysite/urls.py](mysite/mysite/urls.py:19-23):
- `/` → dash app ([dash/urls.py](mysite/dash/urls.py))
- `/polls/` → polls app ([polls/urls.py](mysite/polls/urls.py))
- `/admin/` → Django admin interface

Each app defines its own URL patterns with namespaced routing (`app_name = 'polls'` and `app_name = 'dash'`).

### Database Configuration

The project uses **PostgreSQL** (not SQLite). Database credentials are loaded from environment variables via a `.env` file in [mysite/mysite/settings.py](mysite/mysite/settings.py:82-91):
- `DJANGO_SECRET_KEY`: Django secret key
- `DB_NAME`: Database name (default: `django_polls`)
- `DB_HOST`: Database host (default: `localhost`)
- `DB_USER`: Database user (default: `postgres`)
- `DB_PASSWORD`: PostgreSQL password (required)
- `DB_PORT`: Database port (default: `5432`)

The `.env` file is not in version control. Use [.env.example](.env.example) as a template.

### Template Organization

Templates are organized per-app within each app's `templates/` directory:
- `polls/templates/polls/`: polls_home.html, detail.html, results.html
- `dash/templates/dash/`: index.html

### View Patterns

The polls app demonstrates both view patterns:
- **Function-based views**: `vote()` function for POST handling
- **Generic class-based views**: `IndexView`, `DetailView`, `ResultsView` for standard CRUD operations

Business logic includes filtering future-dated questions (not published yet) in queryset methods.

## Environment Setup

This project uses **uv** for dependency management. The project has both [pyproject.toml](pyproject.toml) and [requirements.txt](requirements.txt) files.

### Initial Setup

```bash
# Install dependencies using uv
uv sync

# Activate the virtual environment
source .venv/bin/activate  # On Linux/Mac
# or
.venv\Scripts\activate  # On Windows
```

### Dependencies

- **Django** (>=3.2, <5.0): Web framework
- **psycopg2-binary** (>=2.9, <3.0): PostgreSQL adapter
- **python-dotenv** (>=1.0.0): Environment variable management

### Environment Configuration

Create a `.env` file in the project root by copying [.env.example](.env.example):

```bash
cp .env.example .env
```

Then edit `.env` with your actual values:
- `DJANGO_SECRET_KEY`: Generate a random secret key for Django
- `DB_PASSWORD`: Your PostgreSQL password
- Other database settings as needed (defaults are provided in [settings.py](mysite/mysite/settings.py:82-91))

## Development Commands

All Django management commands run from the `mysite/` directory:

```bash
cd mysite
```

When using uv, prefix commands with `uv run`:

```bash
uv run python manage.py <command>
```

### Running the Development Server

```bash
uv run python manage.py runserver
```

### Database Operations

```bash
# Apply migrations
uv run python manage.py migrate

# Create new migrations after model changes
uv run python manage.py makemigrations

# Show migration SQL
uv run python manage.py sqlmigrate polls 0001
```

### Testing

```bash
# Run all tests
uv run python manage.py test

# Run specific app tests
uv run python manage.py test polls
uv run python manage.py test dash

# Run specific test class
uv run python manage.py test polls.tests.QuestionModelTests

# Run specific test method
uv run python manage.py test polls.tests.QuestionModelTests.test_was_published_recently_with_future_question
```

### Django Shell

```bash
# Access Django shell for interactive model queries
uv run python manage.py shell
```

### Admin Interface

```bash
# Create superuser for admin access
uv run python manage.py createsuperuser
```

## Key Implementation Details

### Polls App Data Model

The polls app has a Foreign Key relationship:
- `Question` model: question_text, pub_date
- `Choice` model: choice_text, votes, question (ForeignKey)

Questions have a `was_published_recently()` method that checks if pub_date is within the last 24 hours.

### Time-based Query Filtering

Views filter questions using `pub_date__lte=timezone.now()` to exclude future-dated questions. This prevents displaying questions scheduled for future publication.

### Test Coverage

[polls/tests.py](mysite/polls/tests.py) includes:
- Model method tests for `was_published_recently()`
- View tests for IndexView and DetailView
- Test helper function: `create_question(question_text, days)` for creating test data

Tests verify future question filtering and proper display logic.

## Adding New Django Apps

When creating new apps:

1. Create the app: `uv run python manage.py startapp appname`
2. Add app config to `INSTALLED_APPS` in [settings.py](mysite/mysite/settings.py:34-43)
3. Create app's URL patterns with namespace: `app_name = 'appname'`
4. Include app URLs in main [urls.py](mysite/mysite/urls.py)
5. Create app-specific templates directory: `appname/templates/appname/`
