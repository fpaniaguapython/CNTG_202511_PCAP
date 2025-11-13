def get_numeros_impares(numero_maximo):
    for numero in range(1,numero_maximo,2):
        print(f'Proporcionando el número {numero}')
        yield numero # Devuelve el valor de esa iteracción sin abortar el método

for impar in get_numeros_impares(100):
    print(impar)