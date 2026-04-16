from pages.basePage import BasePage

def test_logout(page):
    base_page = BasePage(page)
    base_page.logout()