from faker import Faker

faker = Faker()

pursuitData = {
    "name": f"My Pursuit {faker.word()}",
    "description": faker.sentence(),
    "jupiter_id": "jupiter_101",
    "reference_link": "https://playwright.dev/python/docs/intro",
    "proposal_type": "RFP",
    "type_of_project": "Native Cloud Development",
    "country": "Afghanistan",
    "billing_arrangement": "Fixed Fee"

}