import paquete_1 as p # Importamos las entidades de __init__
from paquete_1 import modulo1 # Importamos modulo1 con su propio nombre (modulo1)
import paquete_2.modulo3 as modulo3 # Importamos paquete_2.modulo3 asignándole un alias

print(p.limite)
modulo1.limite.funcion_1()
modulo3.funcion_3()