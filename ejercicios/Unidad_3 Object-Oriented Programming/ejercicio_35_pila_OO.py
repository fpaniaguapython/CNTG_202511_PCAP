"""
Pila es una estructura de datos --> LIFO (Last In First Out)
Los elementos se introducen por la parte superior (se apilan)
Los elementos se sacan por la parte superior (se desapilan)

Cola es una estructura de datos --> FIFO (First In First Out)
Los elementos se introducen por la parte inferior (se encolan)
Los elementos se sacan por la parte superior (se desencolan)

En Python hay implementaciones de estructuras de datos en
el módulo estándar: collections 
"""

# LIFO
class PilaEnteros:
    def __init__(self):
        self.__data = []

    def push(self, item : int):
        if not isinstance(item, int):
            raise TypeError('La lista solo admite números enteros')
        self.__data.append(item)

    def pop(self) -> int:
        return self.__data.pop()

if __name__=='__main__':
    pila = PilaEnteros()
    pila.push(3)
    pila.push(4)
    pila.push(15)
    pila.push(100)
    item = pila.pop() # 100
    item = pila.pop() # 15
    pila.push(95)
    item = pila.pop() # 95