import uuid
from faker import Faker

fake = Faker()


def generate_uuid():
    return str(uuid.uuid4())


def generate_email():
    return fake.email()


def generate_password():
    return fake.word()
