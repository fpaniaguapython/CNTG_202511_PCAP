# pip install python-Levenshtein
import math
import Levenshtein

# Búsqueda de palabras por proximidad

filosofos = ['Kant', 'Nietzsche', 'Schopenhauer']

palabra_a_buscar = 'Sopenjauer'
print(f'{palabra_a_buscar} encontrada: {palabra_a_buscar in filosofos}')

palabra_a_buscar = 'Nietzsche'
print(f'{palabra_a_buscar} encontrada: {palabra_a_buscar in filosofos}')

palabra_a_buscar = 'Sopenjauer'
distancia_menor = math.inf
for filosofo in filosofos:
    distancia = Levenshtein.distance(palabra_a_buscar, filosofo)
    if (distancia<distancia_menor):
        distancia_menor = distancia
        filosofo_candidato = filosofo
if (distancia_menor==0):
    print(f'Tenemos al filósofo {palabra_a_buscar}')
elif (distancia_menor<4):
    print(f'Pueda que quieras decir {filosofo_candidato}')
else:
    print('No conocemos a ese filósofo')

 