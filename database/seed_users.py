"""Create one admin, one teacher and one student for LOCAL development only.

Run from the project root, with the venv on:   python -m database.seed_users

Passwords must be hashed, which plain SQL can't do, so seeding users is a Python script.
These passwords are for your own laptop only. Never run this on the real server.
"""
from app import create_app
from app.models.user import User

DEV_USERS = [
    ("Dev Admin",   "admin@codeexam.local",   "admin-pass-123",   "admin"),
    ("Dev Teacher", "teacher@codeexam.local", "teacher-pass-123", "teacher"),
    ("Dev Student", "student@codeexam.local", "student-pass-123", "student"),
]

app = create_app()
with app.app_context():
    for name, email, password, role in DEV_USERS:
        if User.find_by_email(email):
            print(f"Already exists: {email}")
            continue
        User.create(name, email, password, role)
        print(f"Created {role}: {email} / {password}")
