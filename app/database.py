"""The Database class (PyMySQL), as in the module lesson, plus one connection per request."""
from contextlib import contextmanager

import pymysql
from flask import current_app, g


class Database:
    def __init__(self):
        cfg = current_app.config
        self.__connection = pymysql.connect(
            host=cfg["MYSQL_HOST"],
            port=cfg["MYSQL_PORT"],
            user=cfg["MYSQL_USER"],
            password=cfg["MYSQL_PASSWORD"],
            database=cfg["MYSQL_DATABASE"],
            cursorclass=pymysql.cursors.DictCursor,   # rows come back as dicts
            autocommit=False,
            charset="utf8mb4",
            init_command="SET time_zone = '+00:00'",  # all times in UTC
        )

    def fetch_one(self, sql, params=()):
        with self.__connection.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchone()

    def fetch_all(self, sql, params=()):
        with self.__connection.cursor() as cur:
            cur.execute(sql, params)
            return cur.fetchall()

    def execute(self, sql, params=()):
        """INSERT / UPDATE / DELETE. Returns the new row id for INSERTs. Does NOT commit."""
        with self.__connection.cursor() as cur:
            cur.execute(sql, params)
            return cur.lastrowid

    @contextmanager
    def transaction(self):
        """Everything inside commits together, or rolls back together on an error."""
        try:
            yield self
            self.__connection.commit()
        except Exception:
            self.__connection.rollback()
            raise

    def close(self):
        self.__connection.rollback()   # throw away anything that was never committed
        self.__connection.close()


def get_db():
    """One connection per request, reused by every model."""
    if "db" not in g:
        g.db = Database()
    return g.db


def close_db(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()
