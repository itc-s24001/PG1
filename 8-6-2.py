import datetime
t_delta = datetime.timedelta(days=1)
dt = datetime.datetime.strptime("21/11/06", "%d/%m/%y")
print(dt + t_delta)
