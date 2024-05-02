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

with open("employees.json") as json_file:
    data = json.load(json_file)

    for emp in data:
        bonus_multiplier = bonus_scale[emp["years_of_experience"]]
        emp["annual_salary"] = round(emp["annual_salary"] * bonus_multiplier, 2)

    for i in range(5):
        print(data[i]["id"], data[i]["annual_salary"])
