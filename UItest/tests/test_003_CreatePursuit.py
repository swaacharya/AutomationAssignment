from pages.createPursuitPage import CreatePursuitPage
from pages.dashboardPage import DashboardPage

from testData.createPursuitData import pursuitData
from testData.createClientData import clientData

clientData = clientData

def test_navigate_to_create_pursuit(page):
    dashboard_page = DashboardPage(page)
    dashboard_page.click_menu_option("Create Pursuit")
    dashboard_page.validatePageText("Create Pursuit")

def test_create_pursuit_with_mandatory_fields(page):
    create_pursuit_page = CreatePursuitPage(page)
    create_pursuit_page.submit_pursuit()
    create_pursuit_page.validatePageText("Resolve all the errors to proceed")

def test_create_client(page):
        create_pursuit_page = CreatePursuitPage(page)
        create_pursuit_page.create_client(clientData["name"])


def test_create_pursuit(page):
    create_pursuit_page = CreatePursuitPage(page)
    pursuit_name = pursuitData["name"]
    pursuit_description = pursuitData["description"]
    create_pursuit_page.create_pursuit(clientData["name"], pursuit_name, pursuit_description)