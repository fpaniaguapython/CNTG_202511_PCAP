import datetime

# Clase: datetime.datetime.date

# Obtener el objeto date correspondiente a HOY
hoy = datetime.date.today()
print(type(hoy)) # <class 'datetime.date'>
print(hoy) # 2025-11-14
print(hoy.year) # 2025
print(hoy.month) # 11
print(hoy.day) # 14

# Construir un date a partir de una fecha
navidad = datetime.date(2025, 12, 25)
print(navidad) # 2025-12-25

# Obtención de un date a partir de un 'timestamp'
import time
ahora_ts = time.time()
print(type(ahora_ts)) # <class 'float'>
print(ahora_ts) # 1763143635.4908943

antes_ts = datetime.date.fromtimestamp(ahora_ts)
print(antes_ts) # 2025-11-14

# Obtención de un date a partir de un fecha en formato ISO
mi_fecha_graduacion = datetime.date.fromisoformat('1999-06-25')
print(mi_fecha_graduacion) # 1999-06-25

# Obtención del día de la semana (lo hicimos en VIERNES)
print(mi_fecha_graduacion.weekday()) # 4 
print(mi_fecha_graduacion.isoweekday()) # 5