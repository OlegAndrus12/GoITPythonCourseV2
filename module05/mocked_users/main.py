from mock import get_mocked_user
import json

filename = input("Enter filename >>> ")
amount = int(input("How many fake users you want >>> "))


with open(filename, "w") as file:
    mocked_users = list()
    for i in range(amount):
        mocked_users.append(json.dumps(get_mocked_user()))
    file.writelines(mocked_users)
