#Import required page
from pages.loginPage import LoginPage

#Import the test data
from testData.loginCred import invalidCred, noCred

def test_user_login_without_credentials(page):
    login = LoginPage(page)

    login.navigateToURL("https://dna-preprod.hashedin.com/pursuits/")
    login.clickSSOLogin()
    login.login_to_persuit(
        noCred["username"],
        noCred["password"]
    )

def test_user_login_with_invalid_credentials(page):
    login = LoginPage(page)

    login.login_to_persuit(
        invalidCred["username"],
        invalidCred["password"]
    ) 
