# Estilo 'tradicional'
fichero = open('./datos.txt', mode='w', encoding='utf-8')
print(type(fichero)) # <class '_io.TextIOWrapper'>
fichero.write('Nos vamos que ya es la hora')
fichero.close()

# Con instrucción with (close es automático)
with open('./datos_with.txt', mode='w', encoding='utf-8') as fichero:
    fichero.write('Ya es la hora')
