"""
- Crear una función que sume dos números decimales (float) positivos DISTINTOS
y devuelva el resultado
- Si alguno de los argumentos no es float, produce un error.
- Si alguno de los argumentos no es positivo, produce un error.
- Si los dos números son iguales, produce un error de tipo ValoresIgualesError
"""

class ValoresIgualesError(ValueError):
    pass

def sumar_numeros_decimales_distintos(sumando_1: float, sumando_2: float) -> float:
    """
    Proporciona la suma de dos números decimales.

    Parameters:
        sumando_1 (float) : Primer sumando.
        sumando_2 (float) : Segundo sumando

    Returns:
        float: Suma de sumando_1 y sumando_2

    Raises:
        ValoresIgualesError : Indica que los dos sumandos son iguales.
    """
    # Validación
    if (not isinstance(sumando_1, float) or not isinstance(sumando_2, float)):
        raise TypeError('Alguno de los sumandos no es un número decimal')
    if (sumando_1<0 or sumando_2<0):
        raise ValueError('Alguno de los sumandos tienen un valor negativo')
    if (sumando_1==sumando_2):
        raise ValoresIgualesError('Los sumandos son iguales')
    # Proceso
    return sumando_1+sumando_2

resultado = sumar_numeros_decimales_distintos(10.3,10.3)
print(resultado)