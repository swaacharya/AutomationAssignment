from faker import Faker

faker = Faker()

clientName = f"My Client {faker.company()}"

clientData = {
    "name": clientName,
    "industry": "Cross Industry",
    "sector": "Not applicable"
}