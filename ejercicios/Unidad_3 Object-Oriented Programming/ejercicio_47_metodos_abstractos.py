# Características de las clases abstractas:
# - Algunos de sus métodos son abstractos:
#   - No están implementados.
#   - Están decorados con @abc.abstractmethod
# - No se puede instanciar.

import abc

# La herencia de abc.ABC indica que la clase es abstracta
class Calculadora(abc.ABC):
    @abc.abstractmethod
    def sumar(self, numero_1, numero_2):
        pass
    
    @abc.abstractmethod
    def restar(self, numero_1, numero_2):
        pass

    def multiplicar(self, numero_1, numero_2):
        return numero_1 * numero_2
    
# c = Calculadora() # Error

class CalculadoraEnteros(Calculadora):
    def sumar(self, numero_1, numero_2):
        return numero_1+numero_2
    
    def restar(self, numero_1, numero_2):
        return numero_1-numero_2
    
class CalculadoraDecimal(Calculadora):
    def sumar(self, numero_1, numero_2):
        return numero_1+numero_2
    
    def restar(self, numero_1, numero_2):
        return numero_1-numero_2

c = CalculadoraEnteros()
print(isinstance(c,Calculadora)) # True
r = c.sumar(5,9)
print(f'Resultado:{r}')

