# Función sin argumentos ni retorno
def escribir_hola_mundo():
    print('Hola mundo')

# Función con argumentos y retorno
def calcular_area(base : int, altura : int) -> int:
    """
    (Esto se llama docstring)
    Calcula el área de un rectángulo

    Parámetros:
    - base: base del rectángulo expresada en centímetros
    - altura: altura del rectángulo expresada en centimetros

    Retorna:
    - int: El área del rectángulo expresada en centímetros
    """
    resultado = base * altura
    return resultado

escribir_hola_mundo()

area = calcular_area(10, 20)
print(area)

# Funciones con valores por defecto
def traducir_texto(texto : str, lengua_origen='ESP', lengua_destino='ENG') -> str:
    pass

traducir_texto('Estoy un curso de Python')
traducir_texto('Estoy un curso de Python','IT')
traducir_texto('Estoy un curso de Python', lengua_origen='FR')
traducir_texto('Estoy un curso de Python', lengua_destino='CN')
traducir_texto('Estoy un curso de Python', lengua_origen='FR', lengua_destino='CN')

# Funciones con parametros variables posicionales
def calcular_distancia(*segmento):
    print(type(segmento)) # <tuple>
    print(segmento)

calcular_distancia(10)
calcular_distancia(10,20)
calcular_distancia(10,20,40)
calcular_distancia(10,20,40,-3)

# Funciones con parámetros variables nombrados o con nombre
def calcular_volumen(**kwargs):
    print(type(kwargs)) # <dict>
    print(kwargs) # {'alto': 10, 'largo': 20, 'ancho': 5}

calcular_volumen(alto=10,largo=20,ancho=5)

# Función con un poco de todo
def funcion_mixta(*args, distancia, ancho=50, **kwargs):
    print("1-",type(args))
    print("2-",args)
    print("3-",distancia)
    print("4-",ancho)
    print("5-",type(kwargs))
    print("6-",kwargs)

funcion_mixta(10, 20, 30, distancia=40, espacio='2D', espacio_destino='3D')