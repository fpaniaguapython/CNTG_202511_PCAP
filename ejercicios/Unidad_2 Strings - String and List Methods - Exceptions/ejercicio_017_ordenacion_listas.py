lista = ['Xbox', 'PlayStation', 'Nintendo']

# Función sorted
lista_ordenada = sorted(lista)
# lista_ordenada = sorted(lista, reverse=True)
print('Lista después de ejecutar la función sorted:', lista) # Lista original con el orden original
print('Lista ordenada después de ejecutar la función sorted:', lista_ordenada) # Nueva lista ordenada

# Método sort
lista.sort()
print('Lista ordenada con método sort:', lista) # Lista original ordenada
lista.sort(reverse=True)
print('Lista ordenada con método sort y reverse=True:', lista) # Lista anterior ordenada al revés