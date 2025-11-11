from ejercicio_35_pila_OO import PilaEnteros

class PilaEnterosAcumulativa(PilaEnteros):
    def __init__(self):
        super().__init__()
        self.acumulado = 0

    # Sobreescritura de método --> Escribir el mismo método en la clase derivada
    def push(self, item):
        super().push(item)
        self.acumulado+=item
    
    # Sobreescritura de método --> Escribir el mismo método en la clase derivada
    def pop(self):
        item = super().pop()
        self.acumulado-=item
        return item

if __name__=='__main__':
    pila = PilaEnterosAcumulativa()
    pila.push(3)
    pila.push(4)
    pila.push(15)
    pila.push(100)
    item = pila.pop() # 100
    item = pila.pop() # 15
    pila.push(95)
    item = pila.pop() # 95