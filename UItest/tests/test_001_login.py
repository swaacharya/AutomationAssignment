#Import required page
from pages.loginPage import LoginPage

#Import the test data
from testData.loginCred import validCred

def test_user_login(page):
    login = LoginPage(page)

    login.navigateToURL("https://dna-preprod.hashedin.com/pursuits/")
    login.clickSSOLogin()
    login.login_to_persuit(
        validCred["username"],
        validCred["password"]
    )

def test_successful_login(page):
    login = LoginPage(page)
    login.validatePageText("Demand Pursuits")
    
