
black_list = ["putin@yandex.com"]
username = input("Username >>> ")

if username.strip() in black_list:
    print("Not allowed. Such user does not exist")
else:
    print("You are welcome")