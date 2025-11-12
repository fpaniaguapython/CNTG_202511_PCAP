# Un método virtual es aquel se que se puede sobreescribir
# en una clase derivada o subclase.
# En Python TODOS los métodos son virtuales
class Calculadora:
    def sumar(self, s1, s2): # virtual (es el que se sobreescribe abajo)
        return s1+s2

class CalculadoraTuneada(Calculadora):
    def sumar(self, s1, s2, s3): # Sobreescritura de método
        return s1+s2+s3

ct = CalculadoraTuneada()
resultado = ct.sumar(1,2)
print(resultado)