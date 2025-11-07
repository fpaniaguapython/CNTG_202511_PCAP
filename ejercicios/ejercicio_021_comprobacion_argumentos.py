class NombreClienteError(ValueError):
    pass

def registrar_cliente(nombre : str, saldo : int):
    """
    Registra un cliente en el sistema.

    Parámetros:
    - nombre : Un str con el nombre del cliente. No pueden ser Steam, Android, Windows.
    - saldo : Un int positivo con el saldo inicial
    """
    # Comienza la validación
    if not isinstance(nombre, str):
        raise TypeError('El nombre tiene que ser un str')
    if not isinstance(saldo, int):
        raise TypeError('El saldo tiene que ser un int')
    if saldo<0:
        raise ValueError('El saldo no puede ser negativo')
    NOMBRES_PROHIBIDOS = ('Steam', 'Android', 'Windows')
    for nombre_prohibido in NOMBRES_PROHIBIDOS:
        if nombre.lower()==nombre_prohibido.lower():
            raise NombreClienteError(f'No se puede utilizar el nombre {nombre}')

    # Comienzo del proceso
    print(f'Registrando al cliente {nombre} con saldo {saldo}')

try:
    registrar_cliente('Guillerme', 10_000)
    # registrar_cliente('Guillerme', -10) # ValueError
    # registrar_cliente('Guillerme', 'diez') # TypeError
    # registrar_cliente(True, 20) # TypeError
    # registrar_cliente('Windows', 5_000) # NombreClienteError
except BaseException as be:
    print(be)
