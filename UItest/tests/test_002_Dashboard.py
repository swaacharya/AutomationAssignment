from pages.dashboardPage import DashboardPage

def test_dashboard_categories(page):
    dashboard = DashboardPage(page)
    dashboard.test_all_category()

def test_parsuit_list_headers(page):
    dashboard = DashboardPage(page)
    headers = ["Client Name", "Initiatives | Pursuit ID", "Jupiter ID", "Country", "Requester", "Proposal Type", "Status", "Start Date", "End Date"]
    dashboard.validateTableHeaders(headers)

def test_menu_container_options(page):
    dashboard = DashboardPage(page)
    dashboard.validate_menu_container_options(["Collapse","Demand Pursuits", "Create Pursuit"])
