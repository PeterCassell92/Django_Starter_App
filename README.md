# Django Starter App

Project built from tutorials in order to better understand Django Framework. This project has been modified to use **uv** for modern Python dependency management.

Original tutorial: https://docs.djangoproject.com/en/5.1/intro/tutorial02/

## Project Structure

This is a multi-app Django project with:
- **polls**: A voting application demonstrating Django models, views, and templates
- **dash**: A dashboard/landing page app

## Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- [uv](https://github.com/astral-sh/uv) package manager

## Getting Started

### 1. Install uv

If you don't have uv installed:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or on Windows:
```bash
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd Django_Starter_App

# Install dependencies
uv sync
```

This will create a `.venv` virtual environment and install Django and PostgreSQL dependencies.

### 3. Configure Database

Create required credential files in `mysite/mysite/`:

**mysite/mysite/secret_key.txt**
```
your-django-secret-key-here
```

**mysite/mysite/pg_admin_pwd.txt**
```
your-postgresql-password-here
```

Ensure your PostgreSQL server is running with:
- Database name: `django_polls`
- User: `postgres`
- Port: `5432`

### 4. Run Migrations

```bash
cd mysite
uv run python manage.py migrate
```

### 5. Create Superuser (Optional)

```bash
uv run python manage.py createsuperuser
```

### 6. Run Development Server

```bash
uv run python manage.py runserver
```

Visit http://localhost:8000 to see the application.

## Development Commands

All commands should be run from the `mysite/` directory with `uv run`:

```bash
# Run tests
uv run python manage.py test

# Run tests for specific app
uv run python manage.py test polls

# Create new migrations
uv run python manage.py makemigrations

# Access Django shell
uv run python manage.py shell

# Create new app
uv run python manage.py startapp appname
```

## Dependencies

- Django (>=3.2, <5.0)
- psycopg2-binary (>=2.9, <3.0)

Dependencies are managed in both `pyproject.toml` and `requirements.txt`.

## Additional Documentation

See [CLAUDE.md](CLAUDE.md) for detailed architecture and development guidance.
