import pytest


@pytest.mark.usefixtures("browser", "page")
class TestLogin:

    @pytest.fixture(scope="class")
    def login_credentials(self):
        return {"username": "your_username", "password": "your_password"}

    def test_login(self, login_credentials, page):
        page.goto("https://example.com/login")

        page.fill('#username', login_credentials["username"])

        page.fill('#password', login_credentials["password"])

        page.click('#login-button')

        user_dashboard_link = page.locator('#user-dashboard-link')

        assert user_dashboard_link.is_visible(), "Login failed: User dashboard link not found."
