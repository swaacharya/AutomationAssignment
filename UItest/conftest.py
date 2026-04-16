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
        page.goto("https://dna-preprod.hashedin.com/pursuits/")
        yield page

        browser.close()

class DataStore:
    data = {}  # Shared across all calls

    @classmethod
    def set_data(cls, key, value):
        cls.data[key] = value

    @classmethod
    def get_data(cls, key):
        return cls.data.get(key)
