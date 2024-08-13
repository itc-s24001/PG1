from datetime import date

day_now = date.today()
print(day_now)

xday = date(2005, 8, 1)
td = day_now - xday
print(td)
