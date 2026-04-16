from playwright.sync_api import expect

class BasePage:
    def __init__(self, page):
        self.page = page
        self.cookiesPopup = self.page.locator('[id="onetrust-close-btn-container"]')

        #table headers locator
        self.tableHeaders = self.page.locator('thead>tr>th>div>span')

        #search bar locator
        self.searchIcon = self.page.locator('[data-icon="search"]')
        self.searchInput = self.page.locator('input[placeholder^="Search"]').nth(0)

        #headers loactor
        self.profile = self.page.locator(".user-profile-container").nth(0)
        self.logoutButton = self.page.locator('text=Logout').nth(0)

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

    def search(self, searchTerm):
        self.page.reload()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)
        self.searchIcon.click()
        self.page.wait_for_timeout(500)
        self.searchInput.fill(searchTerm)

    def validateSearchResults(self, searchTerm, columnIndex):
        searchResults = self.page.locator(f'tbody>tr:nth-child(2)>td:nth-child({columnIndex})')
        print(searchResults.inner_text())
        rowText = searchResults.nth(0).inner_text()
        assert searchTerm in rowText, f"Search term '{searchTerm}' not found in row: {rowText}"

    def logout(self):
        self.profile.click()
        self.logoutButton.click()
        self.validatePageText("Login to continue")
