# from mocker.users.fake_user import get_mocked_user
from mocker import get_mocked_user
import json


filename = input("Filename >>> ")
amount = int(input("How many users >>> "))

with open(filename, "w") as file:
    mocked_users = list()
    for i in range(amount):
        mocked_users.append(json.dumps(get_mocked_user()))
    file.writelines(mocked_users)
