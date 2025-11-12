class Edificacion:
    pass

class Vivienda(Edificacion):
    pass

class Unifamiliar(Vivienda):
    pass

mi_casa = Unifamiliar()

print(issubclass(Unifamiliar, Vivienda)) # True
print(issubclass(Unifamiliar, Edificacion)) # True
print(issubclass(Unifamiliar, object)) # True

print(issubclass(Vivienda, Unifamiliar)) # False

print(isinstance(mi_casa, Unifamiliar)) # True
print(isinstance(mi_casa, Vivienda)) # True
print(isinstance(mi_casa, Edificacion))  # True
print(isinstance(mi_casa, object)) # True

# USOS DE isinstance para verificar tipos : SOLUCIÓN HABITUAL Y RECOMENDADA

def habitar_vivienda(vivienda : Vivienda):
    # Queremos comprar el tipo del objeto vivienda
    if not isinstance(vivienda, Vivienda):
        raise TypeError('El objeto a habitar debe ser de la clase Vivienda')
    print('Habitando vivienda...')

# Recordamos que mi_casa es un objeto de la clase Unifamiliar que hereda de Vivienda
habitar_vivienda(mi_casa)

# Introducimos un 'gazapo'
edificio_hilton = Edificacion()
try:
    habitar_vivienda(edificio_hilton)
except TypeError as te:
    print('No se puede habitar:', te)


# ALTERNATIVA AL USO DE isinstance -> función type # UTILIZAR SOLO CUANDO SEA NECESARIO
# ATENCIÓN: NO TIENE EN CUENTA EL POLIMORFISMO
def habitar_vivienda_alternativa(vivienda : Vivienda):
    if type(vivienda) is not Vivienda:
        raise TypeError('El objeto a habitar debe ser de la clase Vivienda')
    print('Habitando vivienda...')

# habitar_vivienda_alternativa(mi_casa) # Error
mi_vivienda = Vivienda()
habitar_vivienda_alternativa(mi_vivienda) # CORRECTO, pero sólo se comprueba que sea de la clase Vivienda
