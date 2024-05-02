import moskali.utils as utils

from faker import Faker
from pathlib import Path
from moskali.constants import MENU
from moskali.exceptions import NotInRange

FILENAME = Path(__file__).parent / "losses.txt"


def add_new_record(name, amount):
    with open(FILENAME, "a") as f:
        fake = Faker()
        current_date = fake.date_between("-1y").strftime("%m/%d/%Y")
        print(current_date)
        record = f"{current_date: >15}{name: ^40}{amount: ^10}\n"
        f.write(record)


def show_statistics_month(month):
    with open(FILENAME, "r") as f:
        lines = f.readlines()
    res = dict()
    for line in lines:
        date, kind, amount = line.split()
        m = int(date.split("/")[0])
        name_month = utils.get_month_name(m)
        if name_month == month:
            if not kind in res.keys():
                res[kind] = int(amount)
            else:
                res[kind] += int(amount)
    print(f"In {month} we found next data")
    for key, value in res.items():
        print(key, "   ", value)


def show_statistics():
    with open(FILENAME, "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line, end="")


def main():

    calls_dict = {
        1: add_new_record,
        2: show_statistics
    }

    calls_dict[choice]()

    print(MENU)
    while True:
        try:
            choice = int(input("Make your choice please >>> "))
            if choice < 1 or choice > 6:
                raise NotInRange
        except ValueError:
            print("Please write option number")
            continue
        except NotInRange:
            print("choose option from 1-6")
        except:
            print("Whoops, try again")
            continue

        if choice == 1:
            print(f"Please enter data in the following format: <name>:<amount>")
            try:
                s = input(">>> ")
                name, amount = s.strip().split(":")
                add_new_record(name, amount)
            except:
                print("Can not parse your data, try again please")
                continue
        elif choice == 2:
            print("Please see the data below:")
            show_statistics()
        elif choice == 3:
            print("Please enter year")
            try:
                year = int(input(">>> "))
                print(utils.get_calendar_year(year))
            except ValueError:
                print("Add year as an number")
                continue
        elif choice == 4:
            print("Please enter month")
            month = input(">>> ")
            show_statistics_month(month)
        elif choice == 5:
            print(MENU)
        elif choice == 6:
            print("You did great job today! See you")
            break


if __name__ == "__main__":
    main()
