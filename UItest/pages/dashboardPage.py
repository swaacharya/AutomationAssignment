import sys

from pages.basePage import BasePage
import re
from playwright.sync_api import expect

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.catCard = self.page.locator(".ant-card-body")

    def test_all_category(self):
        categories = ["All", "New", "In Progress", "Cancelled", "Won", "Deferred"]
        self.closeCookiesPopup()
        self.validatePageText("Demand Pursuits")
        for cat in categories:
            self.page.wait_for_timeout(2000)
            self.catCard.filter(has_text=cat)
            count = self.catCard.filter(has_text=cat).locator("span").nth(1).inner_text()
            assert count.isdigit() and int(count) >= 0, f"Expected a positive digit, but got: '{count}'"
            print(f"Category: {cat}, Count: {count}")
            
    def testParsuitList(self):
        pass