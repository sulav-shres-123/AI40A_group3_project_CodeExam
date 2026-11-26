"""User model: one row of the users table."""
from werkzeug.security import check_password_hash, generate_password_hash

from app.models.base_model import BaseModel


class User(BaseModel):
    ROLES = ("student", "teacher", "admin")

    def __init__(self, id, name, email, password_hash, role, active):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.active = bool(active)

    @classmethod
    def from_row(cls, row):
        if row is None:
            return None
        return cls(row["id"], row["name"], row["email"], row["password_hash"], row["role"], row["active"])

    @classmethod
    def find_by_id(cls, user_id):
        return cls.from_row(cls.db().fetch_one("SELECT * FROM users WHERE id = %s", (user_id,)))

    @classmethod
    def find_by_email(cls, email):
        return cls.from_row(cls.db().fetch_one(
            "SELECT * FROM users WHERE email = %s", (email.strip().lower(),)))

    @classmethod
    def create(cls, name, email, password, role, active=True):
        if role not in cls.ROLES:
            raise ValueError(f"Unknown role: {role}")
        db = cls.db()
        with db.transaction():
            new_id = db.execute(
                "INSERT INTO users (name, email, password_hash, role, active) VALUES (%s, %s, %s, %s, %s)",
                (name.strip(), email.strip().lower(), generate_password_hash(password), role, int(active)))
        return cls.find_by_id(new_id)

    def set_active(self, active):
        db = self.db()
        with db.transaction():
            db.execute("UPDATE users SET active = %s WHERE id = %s", (int(active), self.id))
        self.active = bool(active)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
