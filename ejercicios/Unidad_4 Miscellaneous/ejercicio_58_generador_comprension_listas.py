lista_consolas = ['Xbox One', 'PlayStation 5', 'Nintendo Switch', 'Super Nintendo', 'Atari 7800']

# CREAMOS UNA LISTA
lista_mayusculas = [consola.upper() for consola in lista_consolas]
print(type(lista_mayusculas)) # <class 'list'>
print(lista_mayusculas) # ['XBOX ONE', 'PLAYSTATION 5', 'NINTENDO SWITCH', 'SUPER NINTENDO', 'ATARI 7800']

# CREAMOS UN GENERADOR EN LUGAR DE UNA LISTA
generador_mayusculas = (consola.upper() for consola in lista_consolas)
print(type(generador_mayusculas)) # <class 'generator'>
for consola_mayusculas in generador_mayusculas:
    print(consola_mayusculas, end=', ')