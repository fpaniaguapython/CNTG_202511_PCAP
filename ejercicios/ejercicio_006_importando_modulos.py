# EN PRIMER LUGAR: IMPORT DE LA BIBLIOTECA ESTÁNDAR
import math # Importamos el módulo entero
# import math as mates # Importamos el módulo entero con un alias (después hay que hacer referencial alias)
# from math import pi # Importamos una entidad concreta sin espacio de nombres
# from math import cos, tan, sin, pi, sqrt # Importamos algunas entidades del módulo sin espacio de nombres
# from math import cos as coseno, tan as tangente, sin as seno
# from math import * # Importamos todas las entidades del módulo sin espacio de nombres - DESACONSEJADO
import random

# EN SEGUNDO LUGAR: IMPORT DE TERCEROS (pueden requerir instalación del paquete con pip)
# import pandas
# import numpy

# EN TERCER LUGAR: IMPORT DE MÓDULOS PROPIOS
import ejercicio_005_calculadora_imc

imc = ejercicio_005_calculadora_imc.calcular_imc(80, 1.7)
print(imc)

pi=3.1416
print(math.pi) # Este es el 'pi de math'
print(pi) # Este es 'nuestro pi'