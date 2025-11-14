import sys

with open('salida_estandar.txt', mode='at', encoding='utf-8') as fichero_output:
    sys.stdout = fichero_output

    print('Esta línea se va a escribir en el "nuevo" stream stdout')