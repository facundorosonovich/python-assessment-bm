from playwright.async_api import Page

from base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    async def navigate_to_profile(self):
        await self.navigate("https://example.com/profile")

    async def verify_user_greeting(self):
        await self.verify_element_text("#greeting", "Welcome, User!")

    async def navigate_to_settings(self):
        await self.click_element("#settings-link")

    async def logout(self):
        await self.click_element("#logout-button")