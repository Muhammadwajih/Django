# Django Project

This repository contains a Django project named MyProject with an app named Myapp.

## Prerequisites
- Python 3.10+
- Git
- Virtual environment support

## Setup
1. Open the project folder:
   ```bash
   cd /path/to/Django
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   ```

   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run database migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and visit:
   ```text
   http://127.0.0.1:8000/
   ```

## Project Structure
- MyProject/ - Django project settings and URLs
- Myapp/ - Application logic, views, templates, and URLs
- db.sqlite3 - SQLite database file

## Useful Commands
- Create a new app:
  ```bash
  python manage.py startapp app_name
  ```

- Create migrations:
  ```bash
  python manage.py makemigrations
  ```

- Apply migrations:
  ```bash
  python manage.py migrate
  ```

- Create a superuser:
  ```bash
  python manage.py createsuperuser
  ```

## Notes
- This project currently uses SQLite, so no additional database setup is required for local development.
- To deactivate the virtual environment later, run:
  ```bash
  deactivate
  ```
