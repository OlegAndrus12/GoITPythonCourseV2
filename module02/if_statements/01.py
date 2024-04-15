# password, username
# admin and guest
# alt + shift + up/down


username = input("Enter your username please")
password = input("Enter your password please")

if username == "admin":
    if password == "qwerty":
        print("Login successful! Welcome admin!")
    elif password == "12345":
        print("Weak password! Change it immediately")
    else:
        print("Incorrect password")
elif username == "guest":
    if password == "guest_sun":
        print("Login successful! Welcome guest!")
    else:
        print("Incorrect password")
else:
    print("go to school!")
