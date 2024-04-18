from datetime import datetime

# %Y: 4-digit year
# %y: 2-digit year
# %m: 2-digit month (01-12)
# %d: 2-digit day of the month (01-31)
# %H: 2-digit hour (00-23)
# %M: 2-digit minute (00-59)
# %S: 2-digit second (00-59)

d = "12-10-2023"
d2 = datetime.strptime(d, "%d-%m-%Y")
print(d2)

d3 = d2.replace(year=2022)
print(d3)

res = d2 - d3
print(res)
print(type(res))
