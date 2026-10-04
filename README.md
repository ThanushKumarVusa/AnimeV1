# Anime World

Simple Flask + MySQL anime login application for DevOps practice.

## Local development

1. Install Python 3, MySQL Server, and Git.
2. Create a MySQL database/user.
3. Run `db/init.sql`.
4. Copy `.env.example` to `.env` and set the database password.
5. Create a virtual environment.
6. Install dependencies: `pip install -r app/requirements.txt`
7. Start: `python app/server.py`
8. Open http://localhost:5000

Demo login:
Username: thanush
Password: anime123

This is a development version. Password hashing and production hardening should be added before production use.
