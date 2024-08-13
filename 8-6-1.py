from datetime import datetime

now = datetime.today()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

dum_day = datetime(2024, 8, 13, hour=14, minute=55, second=49, microsecond=0)
print(dum_day)

dt = datetime.strptime("2024/8/13 15:00", "%Y/%m/%d %H:%M")
print(dt)

dt2 = dt.strftime("%Y年%m月%d日 %H時%M分")
print(dt2)

t_delta = datetime.timedelta(days=1)
print(dt + t_delta)
