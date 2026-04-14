from playwright.sync_api import sync_playwright
import pytest 

@pytest.fixture(scope= "session")
def page():
    headless = False
    
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(
            headless = headless,
            slow_mo = 100
        )

        context = browser.new_context()

        page = context.new_page()
        page.goto("https://google.com/")
        yield page

        browser.close()

