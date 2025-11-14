# Es de más bajo nivel
import time

ahora = time.time() 
print(ahora) # 1763145483.2885613
ahora_gmt = time.gmtime(ahora)
# gmtime proporciona una estructura con toda la información temporal
print(type(ahora_gmt)) # <class 'time.struct_time'>
print(ahora_gmt) # time.struct_time(tm_year=2025, tm_mon=11, tm_mday=14, tm_hour=18, tm_min=39, tm_sec=29, tm_wday=4, tm_yday=318, tm_isdst=0)
print(time.asctime(ahora_gmt)) # Fri Nov 14 18:39:48 2025

# Método sleep detiene la ejecución del programa
print('Pensando',end='')
for i in range(5):
    time.sleep(1)
    print('.',end='')
print('Ya he pensado')