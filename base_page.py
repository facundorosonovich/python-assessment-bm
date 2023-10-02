from playwright.async_api import Page


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    async def navigate(self, url: str):
        await self.page.goto(url)

    async def verify_title(self, expected_title: str):
        actual_title = await self.page.title()
        assert actual_title == expected_title, f"Expected title: {expected_title}, but found: {actual_title}"

    async def verify_element_visible(self, selector: str):
        element = await self.page.query_selector(selector)
        assert element is not None, f"Element with selector '{selector}' is not visible."

    async def verify_element_text(self, selector: str, expected_text: str):
        element = await self.page.query_selector(selector)
        assert element is not None, f"Element with selector '{selector}' is not visible."
        actual_text = await element.text_content()
        assert actual_text == expected_text, f"Expected text: '{expected_text}', but found: '{actual_text}'"

    async def click_element(self, selector: str):
        element = await self.page.query_selector(selector)
        assert element is not None, f"Element with selector '{selector}' is not clickable."
        await element.click()
