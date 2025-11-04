# Crear una función que calcule el IMC (Índice de Masa Corporal)

def calcular_imc(peso : float, altura : float) -> float:
    """
    Calcula el Índice de Masa Corporal. El cálculo se realiza
    dividiendo el peso (expresado en kilogramos) entre la 
    altura (expresada en metros) al cuadrado.

    Parámetros:
    - peso: Peso expresado en kilogramos.
    - altura: Altura expresada en metros

    Retorno:
    - float : El índice de masa corporal
    """
    imc = peso / (altura**2)
    return imc

if __name__=='__main__':
    peso_usuario = float(input('Introduce tu peso (kilogramos):'))
    altura_usuario = float(input('Introduce tu altura (metros):'))

    imc = calcular_imc(peso=peso_usuario, altura=altura_usuario)
    # Escribimos el resultado utilizando f-string
    print(f'Tu IMC (Índice Masa Corporal) es {imc}')