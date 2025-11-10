# Programa Python
# Script Python
# Módulo Python

print('Esto es una sentencia de Python') # Esto es un comentario

# print -> Permite mostrar por consola (salida estándar)
print('Me gusta programar en Python')

# type -> Indica el tipo de la variable
altura=10
print(type(altura)) # <class 'int'>

# bin --> Convierte un <int> a <str> con el formato '0b10101011'
altura = bin(10)
print(altura) # '0b1010'

# hex --> Convierte a hexadecimal
print(hex(10)) # --> '0xa'

# oct --> Convierte a octal
print(oct(10)) # --> '0o12'

# int --> Convierte algo 'convertible' a <int>
print(int('10'))
print(int(8.2))
print(int(True))

# float --> Convierte algo 'convertible' a <float>
print(float(10))
print(float('20.8'))

# str --> Convierte algo 'convertible' a <str>
type(str(10)) # <class 'str'>

# input -> Permite recoger del teclado una entrada. Sólo proporciona <str>
nombre = input('Introduce tu nombre:')
print(nombre)

# len -> Nos indica la longitud de algo 'medible'
print("Longitud:", len('Python'))

# list
# tuple
# set
# dict