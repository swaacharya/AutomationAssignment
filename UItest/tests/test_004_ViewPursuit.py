from pages.viewPursuits import ViewPursuitsPage

from conftest import DataStore

def test_search_pursuit(page):
    view_pursuits_page = ViewPursuitsPage(page)
    pursuit_name = DataStore.get_data("pursuit_name")
    print(pursuit_name)
    view_pursuits_page.search(pursuit_name)
    view_pursuits_page.validateSearchResults(pursuit_name, 2)

def test_view_created_pursuit(page):
    view_pursuits_page = ViewPursuitsPage(page)
    pursuit_name = DataStore.get_data("pursuit_name") if DataStore.get_data("pursuit_name") else DataStore.get_data("searchTerm")
    view_pursuits_page.click_searched_pursuit(pursuit_name)

def test_validate_pursuit_details(page):
    view_pursuits_page = ViewPursuitsPage(page)
    pursuit_data = DataStore.get_data("pursuit_data")
    view_pursuits_page.test_pursuit_details(pursuit_data)