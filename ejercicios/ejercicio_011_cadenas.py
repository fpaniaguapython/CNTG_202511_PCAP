# Las cadenas (tipos <str>) son INMUTABLES

lenguaje = 'Python'
print(lenguaje.upper()) # PYTHON
print(lenguaje) # Python --> ES INMUTABLE
lenguaje = lenguaje.upper()
print(lenguaje) # PYTHON

cadena = 'soy una cadena'
cadena = 'soy \'una\' cadena'
cadena = 'soy "una" cadena'
cadena = "soy otra cadena"
cadena = "soy \"otra\" cadena"
cadena = "soy 'otra' cadena"

cadena = """
Esto es una cadena 
de más de una línea.
Se utiliza para el docstring
y para crear algunas cadenas
cuando son muy largas
"""

cadena = '''
Esto es una cadena 
de más de una línea.
Se utiliza para el docstring
y para crear algunas cadenas
cuando son muy largas
'''

# SLICING
cadena = 'Me gusta programar en Python'
print(cadena[:]) # Toda la cadena -> Desde el principio hasta el final
print(cadena[0:]) # Toda la cadena -> Desde el principio hasta el final
print(cadena[3:6]) # gus -> Desde la posición 3 (empieza por 0), hasta la 5
print(cadena[1:10:2]) # egsap -> Desde la posición 1 hasta la 9, de 2 en 2
print(cadena[0:-1]) # Me gusta programar en Pytho
print(cadena[0:-2]) # Me gusta programar en Pyth
print(cadena[0:-100]) # VACÍO

# Algunos métodos

# find
entrada = '2025#11#06#XUNTA#PYTHON'
print(entrada.find('#')) # 4
print(entrada.find('#',5)) # 7
print(entrada.find('*')) # -1

print('*' in entrada) # False --> RECOMENDADO PARA SABER SI EXISTE O NO UNA SUBCADENA



