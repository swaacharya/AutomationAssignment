class BasePage:
    def __init__(self, page):
        self.page = page

    def navigateToURL(self, url):
        self.page.goto(url)
        self.page.bring_to_front()