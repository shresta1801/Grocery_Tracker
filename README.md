# Grocery Expiry Tracker

A web application for tracking grocery items, expiry dates, and simple expiry-based alerts. Users can register, log in, manage items, view a dashboard with charts, export/import CSV, and adjust preferences such as dark mode and notification windows.

## How this project was built

The app follows a **classic Flask monolith** pattern: one Python module (`app.py`) holds routes, business logic, and SQLAlchemy models together with **Jinja2** templates and **static** HTML, CSS, and JavaScript. That structure keeps the project easy to navigate for coursework or a portfolio piece without introducing extra frameworks.

**Frontend:** Pages under `templates/` (landing, register, login, dashboard, settings, shopping list, shared views) plus assets in `static/` for styling and client-side behavior.

**Backend:** Flask handles routing, sessions, and form handling. **Flask-SQLAlchemy** maps Python classes (`User`, `GroceryItem`) to database tables and performs CRUD through the ORM rather than hand-written SQL in most places.

**Database:** The app is configured for **MySQL** (via PyMySQL and SQLAlchemy). Schema creation is supported through `schema.sql` (fresh installs) and `db.create_all()` when you run the app locally (tables are created if they do not exist).

**Configuration:** Sensitive values (MySQL credentials, `SECRET_KEY`) live in a **`.env`** file loaded with **python-dotenv**. A committed **`.env.example`** documents the required keys without real secrets.

**Deployment-ready pieces:** `requirements.txt` for dependencies, `Procfile` for `gunicorn app:app`, and `runtime.txt` for a Python version on platforms like Render. See `DEPLOYMENT_GUIDE.md` for host-specific steps.

## Features (high level)

- User registration and login (password hashing with Werkzeug)
- Dashboard with active items, expiry grouping, and chart data
- Add, update, delete, and mark items used or completed
- Settings (e.g. dark mode, notification preferences)
- Shopping list and shareable list views
- JSON APIs: expiring soon, filter items, CSV export/import
- Background scheduling hook for notification checks (email path is stubbed until you wire SMTP)

## Tech stack

| Layer        | Technologies                          |
|-------------|----------------------------------------|
| UI          | HTML, CSS, JavaScript, Jinja2 templates |
| Application | Python 3, Flask                       |
| ORM / DB    | Flask-SQLAlchemy, MySQL (PyMySQL)     |
| Server      | Flask dev server locally; Gunicorn in production |

## Project layout

```
├── app.py              # Flask app, models, routes
├── requirements.txt    # Python dependencies
├── schema.sql          # MySQL database + tables
├── .env.example        # Example environment variables (no secrets)
├── Procfile            # gunicorn app:app
├── runtime.txt         # Python version hint for hosts
├── templates/          # Jinja HTML pages
├── static/             # CSS, JS, images
├── tests/              # pytest tests (needs MySQL test DB)
├── view_db.py          # Optional: inspect DB from CLI
├── backup_db.py        # Optional: SQL backup helper (mysqldump)
└── DEPLOYMENT_GUIDE.md # Hosting notes
```

## Local setup

### Prerequisites

- Python 3.10+ (3.11 matches `runtime.txt` for deploys)
- MySQL Server running locally (or a remote instance you can reach)
- Git (optional, for version control)

### 1. Clone and virtual environment

```bash
cd grocery_tracker_Copy   # or your folder name
python -m venv .venv
```

**Windows (PowerShell):**

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### 2. MySQL database

Create the database and tables, for example:

```bash
mysql -u root -p < schema.sql
```

Create a separate empty database for automated tests if you use pytest (e.g. `grocery_tracker_test`).

### 3. Environment variables

```bash
copy .env.example .env
```

Edit `.env` and set at least:

- `MYSQL_HOST`, `MYSQL_USER`, `MYSQL_PASSWORD`, `MYSQL_DATABASE`, `MYSQL_PORT`
- `SECRET_KEY` — use a long random string so sessions stay valid across app restarts

Never commit `.env` (it is listed in `.gitignore`).

### 4. Run the application

```bash
python app.py
```

Open `http://127.0.0.1:5000` in a browser.

If MySQL is not running or credentials are wrong, the app exits with a short error message after failing to connect.

## Tests

Tests expect MySQL. Set `TEST_DATABASE_URL` **or** use the same `MYSQL_*` variables as the app plus `MYSQL_TEST_DATABASE` (default in `tests/conftest.py` is `grocery_tracker_test`).

```bash
pytest tests/
```
