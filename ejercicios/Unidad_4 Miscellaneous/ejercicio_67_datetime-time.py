import datetime

ahora = datetime.time(20, 30, 0)
print(type(ahora)) # <class 'datetime.time'>
print(ahora) # 20:30:00
print(ahora.hour) # 20
print(ahora.minute) # 30
print(ahora.second) # 0