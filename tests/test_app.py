"""Basic checks that the app skeleton starts and is wired up correctly."""


def test_app_uses_the_test_database(app):
    assert app.config["MYSQL_DATABASE"] == "codeexam_test"
    assert app.config["TESTING"] is True


def test_unknown_page_shows_friendly_404(client):
    response = client.get("/this-page-does-not-exist")
    assert response.status_code == 404
    assert b"Page not found" in response.data
