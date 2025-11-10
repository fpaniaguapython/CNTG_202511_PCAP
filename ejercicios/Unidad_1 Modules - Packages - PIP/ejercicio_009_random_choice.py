import random

def leer_ficheros(nombre_fichero : str) -> list:
    with open(nombre_fichero, mode='r', encoding='utf-8') as fichero:
        datos = fichero.readlines()
        datos = [dato.replace('\n','') for dato in datos]
        return datos
    
def generar_persona(nombres_mujer, nombres_hombre, apellidos) -> str:
    # Selecciona una de las dos listas de nombres
    lista_nombres_seleccionada = random.choice((nombres_mujer, nombres_hombre))
    # Selecciona un nombre de la lista seleccionada
    nombre = random.choice(lista_nombres_seleccionada)
    # Selecciona los apellidos de la lista de apellidos
    apellido_1 = random.choice(apellidos)
    apellido_2 = random.choice(apellidos)
    return f'{nombre} {apellido_1} {apellido_2}'

def generar_edad(edad_minima : int, edad_maxima : int):
    edad = random.randint(edad_minima, edad_maxima)
    return edad

if __name__=='__main__':
    NUMERO_PERSONAS = 10
    EDAD_MINIMA = 18
    EDAD_MAXIMA = 67
    nombres_mujer = leer_ficheros('./datos_ejercicio_009/nombres_mujer.txt')
    nombres_hombre = leer_ficheros('./datos_ejercicio_009/nombres_hombre.txt')
    apellidos = leer_ficheros('./datos_ejercicio_009/apellidos.txt')
    # Crear 10 nombres de personas con los datos aleatorios (utilizando random.choice)
    # y con edades aleatorias en un rango determinado
    for i in range(NUMERO_PERSONAS):
        nueva_persona = generar_persona(nombres_mujer, nombres_hombre, apellidos)
        nueva_edad = generar_edad(EDAD_MINIMA, EDAD_MAXIMA)
        print(f'Nombre:{nueva_persona}. Edad:{nueva_edad}')
