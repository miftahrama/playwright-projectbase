"""
Test data generators using Faker.
No print statements - pure utility module.
"""
from faker import Faker

fake = Faker("id_ID")


def generate_data_random() -> dict:
    """Generate random user data."""
    return {
        "username": fake.user_name(),
        "password": fake.password(length=10, special_chars=True),
        "nama_lengkap": fake.name(),
        "email": fake.email(),
        "search_text": fake.word()
        # You can add new line here for create relevan test data as needed
    }