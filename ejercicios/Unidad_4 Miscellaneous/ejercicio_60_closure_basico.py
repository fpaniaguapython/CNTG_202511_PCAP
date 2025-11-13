def externa(nombre):
    nombre_mayusculas = nombre.upper()
    def interna():
        return nombre_mayusculas
    return interna

nombre = 'Estefanía'
funcion_1 = externa(nombre)
nombre = 'Francisco'
funcion_2 = externa(nombre)
print(funcion_1())
print(funcion_2())
