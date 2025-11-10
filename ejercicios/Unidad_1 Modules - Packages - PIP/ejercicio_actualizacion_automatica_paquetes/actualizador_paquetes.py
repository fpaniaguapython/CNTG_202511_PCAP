# pip freeze > requirements.txt

# Forma automática
# pip install -r requirements.txt --upgrade


# Nuestra solución alterinativa
import os

os.system('pip freeze > requirements.txt')

with open('requirements.txt', mode='r') as fichero:
    librerias = fichero.readlines()
    # Obtenemos una lista con los nombres de las librerias
    librerias = [libreria[:libreria.find('==')] for libreria in librerias]
    for libreria in librerias:
        print(f'Actualizando {libreria}')
        os.system(f'pip install -U {libreria}')
    