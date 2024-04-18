from datetime import datetime, timedelta

current = datetime.now()

interval = timedelta(days=2, hours=2)

res = current + interval

print(res)
