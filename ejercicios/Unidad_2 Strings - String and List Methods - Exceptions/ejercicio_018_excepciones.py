# Captura de excepcion
try:
    with open('noexiste.txt', mode='r') as fichero:
        texto=fichero.read() # Lee todo el fichero
        print(texto)
except FileNotFoundError as fnfe:
    print(fnfe) # [Errno 2] No such file or directory: 'noexiste.txt'
print('Final de la ejecución')

# Pedir al usuario un dividendo y un divisor
# Realizar la división, mostrando el resultado
# Capturar y tratar el error que se produce cuando el divisor es 0

dividendo = int(input('Introduce el dividendo:'))
divisor = int(input('Introduce el divisor:'))

try:
    resultado = dividendo/divisor
    print(resultado)
except ZeroDivisionError as zde:
    print('No se puede dividir entre 0')
else:#Opcional
    # print(resultado) # Esta línea estaría activa si no hay un print en el try
    print('Bloque else: se ejecuta únicamente si no hay excepción')
finally:#Opcional
    print('Bloque finally: se ejecuta SIEMPRE')




