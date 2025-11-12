lista = ['cebolla', 'alubia', 'hamburguesa', 'piña']

# Con función tradicional
def mas_de_6_caracteres(alimento):
    return len(alimento)>6

alimentos_saludables = filter(mas_de_6_caracteres, lista)
for alimento in alimentos_saludables:
    print(alimento)
#cebolla
#hamburguesa

# Con función lambda 
alimentos_saludables = filter(lambda alimento : len(alimento)>6, lista)
print(list(alimentos_saludables)) # ['cebolla', 'hamburguesa']
