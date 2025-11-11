class Ordenador:
    cuantico = False
    def __init__(self, marca, modelo, cpu, ram, hd):
        self.marca = marca
        self.modelo = modelo
        self.cpu = cpu
        self.ram = ram
        self.hd = hd

    def agregar_gpu(self, gpu):
        self.gpu = gpu # Añadimos el atributo

    def agregar_raton(self, raton):
        self.raton = raton # Añadimos el atributo

    def eliminar_hd(self):
        del self.hd # Eliminamos el atributo

mi_ordenador = Ordenador('HP', 'Pavilion', 'Ryzen 4000 Series', 16, 256)
mi_ordenador.agregar_gpu('GEFORCE GTX')
mi_ordenador.eliminar_hd()

# print(mi_ordenador.hd) # AttributeError. Lo habíamos eliminado. Hay que gestionar esta posibilidad.

# Alternativa 1 --> Mediante el uso de hasattr
if hasattr(mi_ordenador, 'gpu'):
    print('Tiene GPU')
else:
    print('No tiene GPU')

# Alternativa 2 --> Capturando la excepción AttributeError
try:
    hd = mi_ordenador.hd
    print('Tiene HD')
except AttributeError as ae:
    print('No tiene HD')

# hasattr aplicado a objetos --> aplica a atributos de instancia
print(hasattr(mi_ordenador, 'gpu')) # True
# hasattr aplicado a clases --> aplica a atributos de clase
print(hasattr(Ordenador, 'gpu')) # False
print(hasattr(Ordenador, 'cuantico')) # True