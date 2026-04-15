from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page
        self.cookiesPopup = self.page.locator('[id="onetrust-close-btn-container"]')

        #table headers locator
        self.tableHeaders = self.page.locator('thead>tr>th>div>span')

    def navigateToURL(self, url):
        self.page.goto(url)
        self.page.bring_to_front()
    
    def validatePageText(self, title, eleLoc=None):
        self.page.bring_to_front()
        self.page.wait_for_load_state("networkidle")

        if eleLoc:
            title = eleLoc.get_by_text(title, exact=True)
        else:
            title = self.page.get_by_text(title, exact=True)
        expect(title).to_be_visible()

    def closeCookiesPopup(self):
        self.cookiesPopup.click()

    def validateTableHeaders(self, tableHeaders):
        for i, header in enumerate(tableHeaders):
            headerLocator = self.tableHeaders.nth(i)
            expect(headerLocator).to_be_visible()
            expect(headerLocator).to_have_text(header)
