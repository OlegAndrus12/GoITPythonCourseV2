from datetime import date, timedelta


start_date = date(year=2023, day=12, month=10)
end_date = date(year=2023, day=25, month=10)

days = (end_date - start_date).days + 1
print(days)

for i in range(days):
    res = start_date + timedelta(days=i)
    print(res.strftime("%Y-%m-%d"))
