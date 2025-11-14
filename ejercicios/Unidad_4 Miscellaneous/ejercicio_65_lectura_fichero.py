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