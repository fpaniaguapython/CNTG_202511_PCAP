import calendar

calendario_1971 = calendar.calendar(1971, w=3, l=2, c=0, m=3)
print(calendario_1971)

dia_semana = calendar.weekday(2025,11,14)
print(dia_semana) 

# AÑOS BISIESTOS
print(calendar.isleap(2025)) # False
print(calendar.isleap(2028)) # True
print(calendar.leapdays(2000,2028)) # 7