# Our company has grown so fast this year so we're giving
# every employee with at least five years of experience an
# extra in their annual salary according to the following table
#    5 years = 5%,
#    6 years: 7.5%,
#    7 years: 10,%
#    8 years: 12.5%
#    9 years: 15%
#    1 years': 20%

import json

bonus_scale = {
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1.05,
    6: 1.075,
    7: 1.1,
    8: 1.125,
    9: 1.15,
    10: 1.2,
}


def get_employee_with_bonus(emp):
    bonus_multiplier = bonus_scale[emp["years_of_experience"]]
    emp["annual_salary"] = round(emp["annual_salary"] * bonus_multiplier, 2)
    return emp


with open("employees.json") as json_file:
    data = json.load(json_file)

    employees_with_bonus = list(map(get_employee_with_bonus, data))

    for i in range(5):
        print(employees_with_bonus[i]["id"], employees_with_bonus[i]["annual_salary"])
