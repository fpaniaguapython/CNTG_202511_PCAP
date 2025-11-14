"""
Leer el fichero línea a línea con readline (proporciona una línea en cada lectura) y con readlines (proporciona una lista con todas las líneas)
NOTA: readline devuelve '' cuando llega a final de fichero
1. Comprobar si las líneas leidas tienen \n al final. Si es así, se elimina.
2. Crear una lista con objetos de la clase Producto de aquellos productos con la localización LT-1 con los atributos siguiente:
- id --> product.partNumber
- localizacion --> location.locationIdentifier
- cantidad --> quantity
- valor --> value
3. Obtenemos el importe total (suma de los valores de los objetos) 
"""
from functools import reduce

# Leemos todas las líneas con readlines (incluyen los \n de final de línea)
#with open('datos_min.csv', mode='rt') as fichero:
with open('datos.csv', mode='rt') as fichero:    
    lineas = fichero.readlines()

# Eliminar la cabecera (eliminando la primera línea con un slice)
lineas = lineas[1:]

# Eliminar los \n
lineas = [linea.replace('\n','') for linea in lineas]

# Definir la clase Producto
class Producto:
    def __init__(self, id, localizacion, cantidad, valor):
        self.id = id
        self.localizacion = localizacion
        self.cantidad = cantidad
        self.valor = valor

# Creamos una lista con tuplas con los datos de los productos
lista_componentes_linea = [linea.split(',') for linea in lineas]

# Creamos la lista de Productos cuyas localizaciones son LT-1
productos_lt1 = [Producto(lista_componentes[0], 
                          lista_componentes[1], 
                          lista_componentes[3], 
                          float(lista_componentes[5])) 
                for lista_componentes in lista_componentes_linea if lista_componentes[1]=='LT-1']

# Obtenemos el importe total mediante la función reduce

# Utilizando función convencional
def funcion_reducion(acumulador, elemento : Producto):
    return acumulador + elemento.valor

valor_total = reduce(funcion_reducion, productos_lt1, 0)
print('Valor total con función convencional:', valor_total)

# Utilizando función lambda
valor_total = reduce(lambda acumulador, elemento : acumulador + elemento.valor, productos_lt1, 0)
print('Valor total con función lambda:', valor_total)

# Utilizando función sum
valor_total = sum([producto.valor for producto in productos_lt1])
print('Valor total con la función build-in sum:', valor_total)