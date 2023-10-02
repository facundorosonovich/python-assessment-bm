import pytest


@pytest.fixture(scope="session", autouse=True, params=["chromium", "webkit"])
def set_up_cookie(playwright, request):
    if request.param == "chromium":
        browser = playwright.chromium.launch()
    else:
        browser = playwright.webkit.launch()

    context = browser.new_context(storage_state="state.json", record_video_dir="videos/")
    yield context


@pytest.fixture(scope="session", autouse=True)
def set_up(set_up_cookie):
    context = set_up_cookie
    page = context.new_page()
    page.goto("https://www.backmarket.fr/")
    global PAGE
    PAGE = page
    yield page
    print("-----teardown----")
    page.close()
    context.close()


