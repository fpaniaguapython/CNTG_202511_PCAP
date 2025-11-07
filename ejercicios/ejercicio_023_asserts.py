def sumar(sumando_1 : int, sumando_2 :int) -> int:
    assert isinstance(sumando_1, int)
    assert isinstance(sumando_2, int)
    return sumando_1 + sumando_2
    #return sumando_1 * sumando_2 # Versión con error

def multiplicar(operando_1, operando_2):
    return operando_1 * operando_2

def calcular(operando_1, operando_2, operando_3):
    resultado_parcial = sumar(operando_1, operando_2)
    # La siguiente aserción contiene un mensaje de error personalizado
    assert resultado_parcial==(operando_1+operando_2), 'La función de suma está fallando' # AssertionError: La función de suma está fallando
    resultado_final = multiplicar(resultado_parcial, operando_3)
    return resultado_final

resultado = calcular(3, 8, 15) # 
# resultado = calcular(3.8, 8, 15) # AssertionError
print(resultado) # 165, si no ha ocurrido un AssertionError anteriormente



