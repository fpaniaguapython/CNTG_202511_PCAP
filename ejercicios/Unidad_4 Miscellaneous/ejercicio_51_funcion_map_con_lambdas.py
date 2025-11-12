lista = ['cebolla', 'alubia', 'hamburguesa', 'piña']

# Map con función tradicional
def reemplazar(palabra : str):
    return palabra.replace('a', '@')

resultado = map(reemplazar, lista) # Esta llamada a map aún no ejecuta nada
# resultado es un objeto map que es un iterador
for elemento in resultado:
    print(elemento)
#ceboll@
#@lubi@
#h@mburgues@
#piñ@

# Map con lambda
resultado = map(lambda palabra : palabra.replace('a', '@'), lista)
print(list(resultado)) # Conversión del map a list # ['ceboll@', '@lubi@', 'h@mburgues@', 'piñ@']