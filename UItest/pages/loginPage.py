from pages.basePage import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page

        self.user_name_field = page.locator('[name="username"]').nth(1)
        self.password_field = page.locator('[name="password"]').nth(1)
        self.submit_button = page.locator('[name="signInSubmitButton"]').nth(1)
        self.SOOLoginButton = page.locator('[type="button"]')

    def login_to_persuit(self, username, password):
        self.user_name_field.fill(username)
        self.password_field.fill(password)
        self.submit_button.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        self.closeCookiesPopup()

    def clickSSOLogin(self):
        self.SOOLoginButton.click()

    