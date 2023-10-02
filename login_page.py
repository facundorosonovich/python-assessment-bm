from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    async def navigate_to_login_and_enter_credentials(self, username, password):
        await self.navigate("https://example.com/login")
        await self.page.fill('#username', username)
        await self.page.fill('#password', password)
        await self.click_element('#login-button')

    async def verify_login_success(self):
        await self.verify_element_visible("#user-profile-link")
