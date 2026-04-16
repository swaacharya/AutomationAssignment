from pages.basePage import BasePage

class ViewPursuitsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

    def click_searched_pursuit(self, pursuit_name):
        pursuitLink = self.page.locator(f'text="{pursuit_name}"').nth(0)
        pursuitLink.click()
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

    
    def test_pursuit_details(self, pursuit_data):
        #if individual test case is executed, the created pursuit will not be aviable, so skipping validation in that case
        if not pursuit_data:
            print("No pursuit data found to validate.")
            return
        
        #validating pursuit details with the data used during creation  
        for value in pursuit_data.values():
            print(f"Validating: {value}")
            self.validatePageText(value)