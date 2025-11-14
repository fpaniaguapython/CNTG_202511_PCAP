import datetime

fecha_y_hora = datetime.datetime(year=2025, month=11, day=14, hour=19, minute=20)
print(type(fecha_y_hora)) # <class 'datetime.datetime'>
print(fecha_y_hora) # 2025-11-14 19:20:00
print(fecha_y_hora.day) # 14
print(fecha_y_hora.month) # 11
print(fecha_y_hora.hour) # 19

hoy_y_ahora = datetime.datetime.today()
print(hoy_y_ahora) # 2025-11-14 19:22:30.532007

print(hoy_y_ahora.strftime('%Y')) # 2025
print(hoy_y_ahora.strftime('%d de %B de %Y')) # 14 de November de 2025