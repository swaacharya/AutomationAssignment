from pages.basePage import BasePage

from playwright.sync_api import expect

class DashboardPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        #catergory locator
        self.catCard = self.page.locator(".ant-card-body")

        #side menu panel 
        self.expandMenu = self.page.locator('[alt="Expand"]')
        self.collapseMenu = self.page.locator('[alt="Collapse"]')
        self.menuContainer = self.page.locator('[class^="_menuItemsContainer_"]')

    def test_all_category(self):
        #declaring categories to validate
        categories = ["All", "New", "In Progress", "Cancelled", "Won", "Deferred"]
        self.validatePageText("Demand Pursuits")
        
        #iterating through each category and validating the count is a positive digit
        for cat in categories:
            self.page.wait_for_timeout(500)
            self.catCard.filter(has_text=cat)
            count = self.catCard.filter(has_text=cat).locator("span").nth(1).inner_text()
            assert count.isdigit() and int(count) >= 0, f"Expected a positive digit, but got: '{count}'"
            print(f"Category: {cat}, Count: {count}")

    def validate_menu_container_options(self, options):
        self.expandMenu.click()
        for option in options:
            self.validatePageText(option, self.menuContainer)
        self.collapseMenu.click()

    def click_menu_option(self, option):
        self.expandMenu.click()
        option_locator = self.menuContainer.locator(f"text={option}")
        expect(option_locator).to_be_visible()
        option_locator.click()