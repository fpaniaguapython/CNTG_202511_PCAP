with open('quijote.txt', mode='r', encoding='utf-8') as fichero:
    texto_original = fichero.read() # Leemos todo el fichero
    texto = texto_original
# Obtener el número de palabras distintas
print('****:',texto_original.lower().count('dulcinea')) # 285, incluyendo dulcineae, dulcineas y dulcineas
print('****:',texto_original.lower().count('sancho')) # 2150, incluyendo sanchos y sanchos
print('****:',texto_original.lower().count('por')) # 5530

# Eliminar los caracteres no válidos
caracteres_no_validos = '»,.:;"\'¿?¡!-\n'

for caracter_no_valido in caracteres_no_validos:
    texto = texto.replace(caracter_no_valido, ' ')

# Obtener los token, previa conversión del texto a minúscula con lower
palabras = texto.lower().split() # palabras es una lista
print(f'Hemos encontrado {len(palabras)} palabras')

# Meter las palabras en un diccionario para eliminar duplicados
diccionario_palabras = set(palabras)
print(f'Hemos encontrado {len(diccionario_palabras)} palabras distintas')

# Obtener el número de veces que aparecen las palabras Sancho, Dulcinea y por
numero_sancho = palabras.count('sancho')
numero_dulcinea = palabras.count('dulcinea')
numero_por = palabras.count('por')

print('Número de veces que aparece Sancho:', numero_sancho)
print('Número de veces que aparece Dulcinea:', numero_dulcinea)
print('Número de veces que aparece por:', numero_por)