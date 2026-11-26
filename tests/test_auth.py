"""Login and logout tests (US-01 and US-11 acceptance criteria)."""
from app.models.user import User
from tests.conftest import STUDENT, TEACHER


def test_login_page_loads(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Log in" in response.data


def test_home_requires_login(client):
    response = client.get("/")
    assert response.status_code == 302
    assert "/login" in response.headers["Location"]


def test_teacher_can_log_in(client, login):
    response = login(TEACHER)
    assert response.status_code == 302
    home = client.get("/")
    assert home.status_code == 200
    assert b"Test Teacher" in home.data


def test_wrong_password_shows_generic_message(client):
    response = client.post("/login", data={"email": TEACHER["email"], "password": "wrong"})
    assert response.status_code == 401
    assert b"Wrong email or password." in response.data


def test_unknown_email_shows_the_same_message(client):
    response = client.post("/login", data={"email": "nobody@test.local", "password": "whatever"})
    assert response.status_code == 401
    assert b"Wrong email or password." in response.data


def test_deactivated_user_cannot_log_in(app, client):
    with app.app_context():
        User.find_by_email(STUDENT["email"]).set_active(False)
    response = client.post("/login", data={"email": STUDENT["email"], "password": STUDENT["password"]})
    assert response.status_code == 401


def test_passwords_are_hashed(app):
    with app.app_context():
        user = User.find_by_email(TEACHER["email"])
    assert user.password_hash != TEACHER["password"]
    assert user.check_password(TEACHER["password"])


def test_logout_needs_post(client, login):
    login(TEACHER)
    assert client.get("/logout").status_code == 405
    response = client.post("/logout")
    assert response.status_code == 302
    assert client.get("/").status_code == 302      # logged out → back to login


def test_login_ignores_outside_next_links(client):
    response = client.post("/login?next=//evil.example",
                           data={"email": TEACHER["email"], "password": TEACHER["password"]})
    assert response.headers["Location"] == "/"
