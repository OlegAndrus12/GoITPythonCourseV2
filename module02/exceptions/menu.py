menu = """
    #1: open tiktok
    #2: open instagram
    #3: play frisbee with dog
    #4: do coding
    #5: exit
"""

print(menu)

while True:
    try:
        choice = int(input("What would you like >>> "))
        if choice > 5 or choice < 1:
            raise Exception("Please choose an option from menu [1-5]")
        match choice:
            case 1:
                print("tiktok")
            case 2:
                print("instagram")
            case 3:
                print("horray!!! Catch the frisbee")
            case 4:
                print("VScode is waiting for you")
            case _:
                print("nothing")
    except ValueError:
        print("Please enter a number")
        continue
    except Exception as e:
        print(e)
        continue

    if choice == 5:
        break
