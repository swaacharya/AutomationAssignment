from pages.dashboardPage import DashboardPage

def test_dashboard_categories(page):
    dashboard = DashboardPage(page)
    dashboard.test_all_category()