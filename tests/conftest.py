"""Shared test setup: a fresh codeexam_test database for every test."""
from pathlib import Path

import pymysql
import pytest

import config
from app import create_app

TEST_DB = "codeexam_test"
SCHEMA_FILE = Path(__file__).resolve().parent.parent / "database" / "schema.sql"


def _sql_statements(text):
    """Split schema.sql into single statements (drops -- comment lines)."""
    lines = [line for line in text.splitlines() if not line.strip().startswith("--")]
    return [part.strip() for part in "\n".join(lines).split(";") if part.strip()]


def _reset_test_database():
    assert TEST_DB.endswith("_test"), "Refusing to wipe a database that isn't a test database"
    connection = pymysql.connect(host=config.MYSQL_HOST, port=config.MYSQL_PORT,
                                 user=config.MYSQL_USER, password=config.MYSQL_PASSWORD,
                                 charset="utf8mb4", autocommit=True)
    try:
        with connection.cursor() as cur:
            # TEST_DB is a constant, never user input, so formatting it in is safe here
            cur.execute(f"DROP DATABASE IF EXISTS `{TEST_DB}`")
            cur.execute(f"CREATE DATABASE `{TEST_DB}` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            cur.execute(f"USE `{TEST_DB}`")
            for statement in _sql_statements(SCHEMA_FILE.read_text(encoding="utf-8")):
                cur.execute(statement)
    finally:
        connection.close()


@pytest.fixture
def app():
    _reset_test_database()
    app = create_app({
        "TESTING": True,
        "MYSQL_DATABASE": TEST_DB,
        "WTF_CSRF_ENABLED": False,      # tests don't send CSRF tokens
        "SESSION_COOKIE_SECURE": False,
    })
    yield app


@pytest.fixture
def client(app):
    return app.test_client()
