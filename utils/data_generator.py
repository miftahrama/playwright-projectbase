"""
Test data generators using Faker.
No print statements - pure utility module.
"""
from faker import Faker

fake = Faker("id_ID")


def generate_user_data() -> dict:
    """Generate random user registration data."""
    return {
        "username": fake.user_name(),
        "password": fake.password(length=10, special_chars=True),
        "nama_lengkap": fake.name(),
        "email": fake.email(),
    }


def generate_login_credentials() -> dict:
    """Generate random login credentials."""
    return {
        "username": fake.user_name(),
        "password": fake.password(length=12, special_chars=True),
    }


def generate_school_data() -> dict:
    """Generate random school data."""
    return {
        "school_name": f"SMP - {fake.city()}",
        "search_text": fake.word(),
    }