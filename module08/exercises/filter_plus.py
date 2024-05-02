import json


def lesser_than(object, key, n_years):
    return True if object[key] <= n_years else False


with open("employees.json") as json_file:
    data = json.load(json_file)

    # 1. let's get all employees with less than 3 years of experience

    employees_3_years_of_experience = list(
        filter(lambda emp: lesser_than(emp, "years_of_experience", 3), data)
    )

    print(
        f"Employees with less than 3 years of experience:{len(employees_3_years_of_experience)}"
    )

    # 2. let's get all employees with less than 3 years of experience
    # and less than 25 years

    employees_3_years_of_experience_and_less_than_25_years = list(
        filter(lambda emp: emp["years_of_experience"] <= 3 and emp["age"] <= 25, data)
    )

    print("Employees with less than 3 years")
    print(
        f"of experience and less than 25 years:{len(employees_3_years_of_experience_and_less_than_25_years)}"
    )

    # 3. let's get all employees that don't have a shirt size :(

    employees_with_no_shirt_size = list(filter(lambda emp: not emp["shirt_size"], data))

    print(f"Employees with no shirt size:{len(employees_with_no_shirt_size)}")
