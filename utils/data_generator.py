from faker import Faker

fake = Faker('id_ID')  # Menggunakan lokal Indonesia jika perlu nama/data lokal

def generate_user_registration_data():
    """generate satu set data acak untuk registrasi."""
    return {
        "username": fake.user_name(),
        "password": fake.password(length=10, special_chars=True),
        "nama_lengkap": fake.name(),
        "email": fake.email()
    }

print(generate_user_registration_data())