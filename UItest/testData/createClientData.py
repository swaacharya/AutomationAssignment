from faker import Faker

faker = Faker()

clientName = f"My Client {faker.company()}"

clientData = {
    "name": clientName,
}