# nombres_mujer
# nombres_hombre 
# apellidos

def leer_ficheros(nombre_fichero : str) -> list:
    with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
        datos = fichero.readlines()
        datos = [dato.replace('\n','') for dato in datos]
        return datos
    
def generar_persona(nombres_mujer, nombres_hombre, apellidos):
    pass

def generar_edad(edad_minima : int, edad_maxima : int):
    pass

if __name__=='__main__':
    nombres_mujer = leer_ficheros('./datos_ejercicio_009/nombres_mujer.txt')
    nombres_hombre = leer_ficheros('./datos_ejercicio_009/nombres_hombre.txt')
    apellidos = leer_ficheros('./datos_ejercicio_009/apellidos.txt')
    # Crear nombres de personas con los datos aleatorios (utilizando random.choice)
    # y con edades aleatorias en un rango determinado
