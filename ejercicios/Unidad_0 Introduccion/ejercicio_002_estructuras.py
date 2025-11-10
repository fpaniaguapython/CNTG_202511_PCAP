# Listas:
# Delimitadores son []
# Función para crear listas es la función list
# Mantiene orden
# Tipos de elemento son heterogéneos
# Es 'mutable'
# Es 'iterable' (se puede recorrer con un for)
# Admite el operador in
dias_semana = ['Luns', 'Martes', 'Mercores', 'Xoves', 'Venres', 'Sábado', 'Domingo']
meses_anyo = list() # Crea una lista vacía
meses_anyo.append('Enero')
print(meses_anyo[0]) # 'Enero'
meses_anyo[0]='Xaneiro'
print(meses_anyo[0]) # Xaneiro'
meses_anyo.append('Febreiro')
for mes in meses_anyo:
    print(mes)
# Añadir al final de la lista (append) los meses Marzo, Abril, Mayo, Junio
meses_anyo.append('Marzo')
meses_anyo.append('Abril')
meses_anyo.append('Mayo')
meses_anyo.append('Junio')
# Cambiar los nombres de los meses por los nombres en gallego (los que aplique)
meses_anyo[4]='Maio'
meses_anyo[5]='Xuño'
# Mostrar los meses con un bucle for
for mes in meses_anyo:
    print(mes)
# Insertar un elemento
meses_anyo.insert(1,'Otra cosa') # Inserta en una posición concreta
# Eliminar un elemento indicando el contenido
meses_anyo.remove('Otra cosa') # Elimina el elemento indicado
# Eliminar un elemento indicando la posición obteniendo dicho elemento (como un cortar y pegar)
meses_anyo.insert(2,'Otro más')
elemento = meses_anyo.pop(2)

print('Mayo' in meses_anyo) # Indica si existe o no un elemento

# Tupla
# Delimitadores son ()
# Función para crear tuplas es la función tuple
# Mantiene orden
# Tipos de elemento son heterogéneos
# Es 'INMUTABLE'
# Es 'iterable' (se puede recorrer con un for)
# Admite el operador in
horas = (1,3,5,11)
for hora in horas:
    print(hora)

tupla_con_un_elemento = ('Algo',) # Sin coma, es una expresión
print(type(tupla_con_un_elemento))

# Conjunto
# Delimitadores son {}
# Función para crear conjunots es la función set
# No hay orden
# No admite duplicados
# Tipos de elemento son heterogéneos
# Es 'mutable'
# Es 'iterable' (se puede recorrer con un for)
# Admite el operador in
frutas_invierno = {'Naranja', 'Limón', 'Fresa', 'Naranja', 'Limón'}
print('Piña' in frutas_invierno)

frutas_verano = {'Melón', 'Sandía', 'Naranja'}

for fruta in frutas_invierno:
    print(fruta)

frutas_invierno.add('Uva')

frutas_todo_anyo = frutas_invierno.intersection(frutas_verano)
print(type(frutas_todo_anyo))
print(frutas_todo_anyo)

# Diccionario
# Claves NO se pueden repetir
# Valores SÍ se pueden repetir
diccionario_rae = {
    'programa':'Edicto, bando o aviso público.', 
    'resumen':'Acción y efecto de resumir o resumirse.',
    'ocio':'Cesación del trabajo, inacción o total omisión de la actividad.'}

print(diccionario_rae['programa']) # Si la clave no existe -> KeyError
print(diccionario_rae.get('plaza')) # Si la clave no existe -> Devuelve None
print(diccionario_rae.get('plaza','No tengo esa clave')) # Si la clave no existe -> Devuelve el valor por defecto

diccionario_rae['ocio']='Tiempo libre de una persona.' # Asignación

print('*** KEYS ***')
print(diccionario_rae.keys())

print('*** VALUES ***')
print(diccionario_rae.values())

print('*** ITEMS ***')
print(diccionario_rae.items())

for palabra in diccionario_rae.keys():# Recorre las claves
    print(palabra)

for descripcion in diccionario_rae.values():# Recorre los valores
    print(descripcion)

for palabra, descripcion in diccionario_rae.items():# Recorre claves y valores
    print(palabra, descripcion)

print(len(diccionario_rae)) # Devuelve el número de items
print('programax' in diccionario_rae) # Nos dice si la clave está en el diccionario

# NOTA EXTRA
# Las funciones list(), tuple(), set() y dict() sirven para crear o convertir estructuras de datos