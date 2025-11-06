def dividir(dividendo, divisor):
    if (divisor==0):
        raise ValueError('No seas brut@, no se puede dividir entre cero')
    resultado = dividendo/divisor
    return resultado

try:
    el_resultado = dividir(10,2)
    print(el_resultado)
except ValueError as ve:
    print(ve)

