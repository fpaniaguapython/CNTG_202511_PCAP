"""
Crear una clase Factura.
- En el __init__ se crean los atributos 'numero','cliente','fecha'
-Dispone de un metodo agregar_importe que recibe un entero y lo suma
al atributo importe (se crea en este método si no existe)

En el __main__:
- Crear una factura y agregar varios importes.
- Crear otra factura sin importes.
- Meterlas en una list
- Mostrar el importe total de las facturas (si existe dicho importe)
"""

class Factura:
    def __init__(self, numero, cliente, fecha):
        self.numero = numero
        self.cliente = cliente
        self.fecha = fecha
    
    def agregar_importe(self, cantidad):
        if (hasattr(self, 'importe')):
            self.importe = self.importe + cantidad
        else:
            self.importe = cantidad


f1 = Factura('001', 'Cliente 1', '11/11/2025')
f1.agregar_importe(100)
f1.agregar_importe(50)
f1.agregar_importe(3)

f2 = Factura('002', 'Cliente 2', '10/11/2025')

facturas = [f1, f2]
for factura in facturas:
    if hasattr(factura, 'importe'):
        print(f'La factura {factura.numero} tiene como importe {factura.importe}')
    else:
        print(f'La factura {factura.numero} no tiene importe')