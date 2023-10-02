
class HomePage:
    def __init__(self, page):
        self.page = page
        self.login_button = page.locator('login-button')

    async def navigate_to_profile(self):
        await self.page.goto("https://example.com/profile")

    async def navigate_to_login(self):
        await self.login_button.click()
