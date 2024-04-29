from faker import Faker

fake = Faker()

def get_mocked_text():
    return fake.text()

def get_mocked_sentence():
    return fake.sentence()