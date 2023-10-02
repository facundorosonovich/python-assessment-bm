from base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    async def navigate_to_login(self):
        await self.navigate("https://example.com/login")

    async def enter_username(self, username):
        await self.page.fill('#username', username)

    async def enter_password(self, password):
        await self.page.fill('#password', password)

    async def click_login_button(self):
        await self.click_element('#login-button')

    async def verify_login_success(self):
        await self.verify_element_visible("#user-profile-link")

    async def login(self, username, password):
        await self.navigate_to_login()
        await self.enter_username(username)
        await self.enter_password(password)
        await self.click_login_button()
