# Password and Username Checking
username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "admin":
    if password == "password":
        print("Login successful! Welcome, admin.")
    elif password == "12345":
        print("Weak password. Please reset your password.")
    else:
        print("Incorrect password. Please try again.")
else:
    if username == "guest":
        if password == "guest":
            print("Login successful! Welcome, guest.")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("Unknown user. Please try again.")


# Using if-else for Validation
name = input("Enter your name: ")
email = input("Enter your email address: ")
password = input("Enter your password: ")

if name == "":
    print("Name cannot be empty.")
else:
    if "@" not in email:
        print("Invalid email address.")
    else:
        if len(password) > 8:
            print("Password must be at least 8 characters long.")
        else:
            print("Registration successful.")
