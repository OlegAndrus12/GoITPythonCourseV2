import random
from faker import Faker

fake = Faker()


def get_mocked_user():
    fake = Faker()
    mock = {
        "user_id": fake.unique.random_int(min=1, max=1000),
        "name": fake.name(),
        "last_name": fake.last_name(),
        "email_address": fake.email(),
        "phone_number": fake.phone_number(),
        "date_joined": fake.date_time().strftime("%m/%d/%Y, %H:%M:%S"),
    }
    return mock


if __name__ == "__main__":
    mock = get_mocked_user()
    print(mock)
