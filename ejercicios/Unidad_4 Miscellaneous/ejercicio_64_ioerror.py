"""
En este ejercicio se intenta abrir en modo 'r' un fichero inexistente.

El sistema lanza un IOError cuyo atributo errno es errno.ENOENT, que 
indica que el fichero o el directorio no existe.

A través de la función strerror del módulo os se puede obtener
información de la constante del error (errno.ENOENT en este caso)

NOTA: errno.ENOENT se encuentra en el módulo errno
"""
import errno
import os

try:
    with open('fichero_inexistente.txt', mode='r') as fichero:
        print('Fichero abierto')
except IOError as ioe:
    print(ioe) # [Errno 2] No such file or directory: 'fichero_inexistente.txt'
    if (ioe.errno==errno.ENOENT):
        print('Has intentado abrir un directorio como si fuese un fichero')
        print(os.strerror(ioe.errno)) # No such file or directory    