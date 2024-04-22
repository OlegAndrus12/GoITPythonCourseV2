mystr = '12345'
print(mystr.isdigit())

mystr = '10.5'
print(mystr.isdigit())

mystr = 'python'
print(mystr.isdigit())


pay_system = {5: "MasterCard", 4: "Visa", 3: "American Express"}

card_number = ["5375414112345678", "4168757587879876", "216875758787987d"]


def isvalid_card(card):
    # ^[0-9]{16}$
    return card.isdigit() and len(card) == 16



def is_float(string):
    if string.replace(".", "").isnumeric():
        return True
    else:
        return False

print(is_float('1.23')) # True
print(is_float('123')) # True
print(is_float('1.23a')) # False


def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

print(is_float('1.23'))
print(is_float('123'))
print(is_float('1.23a')) 
