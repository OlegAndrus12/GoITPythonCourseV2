import json

with open("employees.json") as json_file:
    data = json.load(json_file)

    # 1. let's get all employees with less than 3 years
    # of experience

    employees_filtered = []

    for employee in data:
        if employee["years_of_experience"] <= 3:
            employees_filtered.append(employee)

    print(f"Employees with less than 3 years of experience:{len(employees_filtered)}")

    # 2. let's get all employees with less than 3 years of experience
    # and less than 25 years

    employees_3_years_and_25_years = []

    for employee in data:
        if employee["years_of_experience"] <= 3 and employee["age"] <= 25:
            employees_3_years_and_25_years.append(employee)

    print(
        f"""Employees with less than 3 years of experience
        and less than 25 years:{len(employees_3_years_and_25_years)}"""
    )

    # 3. let's get all employees that don't have a shirt size :(

    employees_with_no_shirt_size = []

    for employee in data:
        if not employee["shirt_size"]:
            employees_with_no_shirt_size.append(employee)

    print(f"Employees with no shirt size:{len(employees_with_no_shirt_size)}")
