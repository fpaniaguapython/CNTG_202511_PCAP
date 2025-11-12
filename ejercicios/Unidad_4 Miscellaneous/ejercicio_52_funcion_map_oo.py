class Factura:
    def __init__(self, numero, numero_productos, precio_unitario):
        self.numero = numero
        self.numero_productos = numero_productos
        self.precio_unitario = precio_unitario

f1 = Factura(1, 10, 100)
f2 = Factura(2, 20, 5)
f3 = Factura(3, 5, 1000)

facturas = [f1, f2, f3]

# Utilizando map, obtener tuplas con el número de la factura y el importe

resumen_facturas = map(lambda factura : (factura.numero, factura.numero_productos*factura.precio_unitario), facturas)
for resumen in resumen_facturas:
    print(resumen)