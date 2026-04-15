from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page
        self.cookiesPopup = self.page.locator('[id="onetrust-close-btn-container"]')

    def navigateToURL(self, url):
        self.page.goto(url)
        self.page.bring_to_front()
    
    def validatePageText(self, title):
        self.page.bring_to_front()
        self.page.wait_for_load_state("networkidle")

        title = self.page.get_by_text(title, exact=True)
        expect(title).to_be_visible()

    def closeCookiesPopup(self):
        self.cookiesPopup.click()

    def validateTableHeaders(self, tableHeaders):
        pass