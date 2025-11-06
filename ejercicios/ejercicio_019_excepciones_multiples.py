
try:
    lista =[1, 2]
    resultado = lista[0]/lista[1]
    print(resultado) # 0.5
    lista[1]=0
    resultado = lista[0]/lista[1] # ZeroDivisionError
    print(resultado) # 0.5
    lista[2]=10 # IndexError
except ZeroDivisionError as zde:
    print('Error:', zde)
except IndexError as ie:
    print('Error:', ie)
except Exception as ex:
    print('Ha ocurrido un error desconocido')
else:
    # Este es el código que se ejecuta si no hay excepción
    pass
finally:
    # Este es el código que se ejecuta SIEMPRE
    pass