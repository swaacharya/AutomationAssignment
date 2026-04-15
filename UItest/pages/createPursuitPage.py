from pages.basePage import BasePage

from testData.Date import Date
from testData.createPursuitData import pursuitData

class CreatePursuitPage(BasePage):
    def __init__(self, page):
        super().__init__(page)

        #create pursuit locators
        self.pursuit_name_input = self.page.locator('[placeholder="Enter pursuit name"]')

        self.proposal_type = self.page.locator('[id^="rc_select_"]').nth(1)
        self.proposal_type_option_0 = self.page.get_by_text("RFP").nth(1)

        self.type_of_project = self.page.locator('[id^="rc_select_"]').nth(2)
        self.type_of_project_option_0 = self.page.get_by_text("Native Cloud Development").nth(1)

        self.country_field = self.page.locator('[id^="rc_select_"]').nth(3)
        self.country_option_0 = self.page.get_by_text("Afghanistan").nth(1)

        self.billing_arragement = self.page.locator('[id^="rc_select_"]').nth(4)
        self.billing_arragement_0 = self.page.get_by_text('Fixed Fee').nth(1)
        
        self.project_start_date = self.page.locator('[date-range="start"]')
        self.project_end_date = self.page.locator('[date-range="end"]')
        self.done_button = self.page.get_by_role("button", name="Done")

        self.jupiter_id_input = self.page.locator('[placeholder="Enter jupiter ID"]')

        
        self.pursuit_description_input = self.page.locator('.ql-editor').nth(0)
        self.reference_links_input = self.page.locator('.ql-editor').nth(1)

        self.save_button = self.page.get_by_role("button", name="Create", exact=True)

        #create client locators
        self.create_client_button = self.page.get_by_text("Add New Client")
        self.client_name_input = self.page.locator('[placeholder="Add New Client"]')

        self.industry_field = self.page.locator('.dna-modal-body [id^="rc_select_"]').nth(0)
        self.industry_option_0 = self.page.get_by_text("Cross Industry").nth(1)

        self.sector_field = self.page.locator('.dna-modal-body [id^="rc_select_"]').nth(1)
        self.sector_option_0 = self.page.get_by_text("Not applicable").nth(1)

        self.save_client_button = self.page.get_by_role("button", name="Save")

    def create_client(self, client_name):
        self.create_client_button.click()
        self.client_name_input.fill(client_name)

        self.page.wait_for_timeout(2000)

        self.industry_field.click()
        self.industry_option_0.click()

        self.page.wait_for_timeout(500)

        self.sector_field.click()
        self.sector_option_0.click()

        self.save_client_button.click()

    def create_pursuit(self, client_name, name, description):
        self.pursuit_name_input.fill(name)

        self.proposal_type.click()
        self.proposal_type_option_0.click()

        self.type_of_project.click()
        self.type_of_project_option_0.click()

        self.country_field.click()
        self.country_option_0.click()

        self.billing_arragement.click()
        self.billing_arragement_0.click()

        self.project_start_date.click()
        self.page.locator(f"[title=\"{Date['today']}\"]").click()
        self.page.locator(f"[title=\"{Date['todayplus30']}\"]").click()
        self.done_button.click()

        # self.page.evaluate(f"document.querySelector('{self.project_start_date}').value = '{Date['today']}'")
        # self.page.evaluate(f"document.querySelector('{self.project_end_date}').value = '{Date['todayplus30']}'")

        self.jupiter_id_input.fill(pursuitData["jupiter_id"])

        self.pursuit_description_input.fill(description)
        self.reference_links_input.fill(pursuitData["reference_link"])

        self.save_button.click()

        self.validatePageText("Successfully submitted")
