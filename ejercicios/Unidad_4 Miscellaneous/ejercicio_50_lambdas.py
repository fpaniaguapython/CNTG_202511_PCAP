# Función tradicional
def sumar(s1, s2):
    return s1+s2

resultado = sumar(10,1)
print(resultado)

# Función lambda "con nombre" (la funciones lambda no tienen nombres) (NO EL USO HABITUAL)
restar = lambda n1, n2 : n1-n2
print(restar(8,3))

# Ejecución de lambda sin asignación (NO EL USO HABITUAL)
print((lambda n1, n2 : n1-n2)(5,8))

# Función lambda que convierta una cadena de caracteres a mayúsculas
# Solución de Manuel
mayus = lambda texto: texto.upper()
print(mayus("prueba mayus")) # PRUEBA MAYUS

# Función lambda que proporcione el número de elementos de una lista
# Solución de David F.
numero = lambda lista : len(lista)
print(numero([1,8,4,'otro',True]))

# Función lambda  que indique si un número es mayor que otro
# Solución Lara (muy compacta)
print((lambda n1,n2 : n1 > n2)(2,4)) # False
# Solución más explícita
funcion_comparacion = lambda n1,n2 : n1>n2
resultado = funcion_comparacion(2,4)
print(resultado) # False