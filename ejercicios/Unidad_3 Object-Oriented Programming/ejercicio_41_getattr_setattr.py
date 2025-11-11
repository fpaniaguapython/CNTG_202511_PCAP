class Ordenador:
    def __init__(self, marca, modelo, cpu, ram, hd):
        self.marca = marca
        self.modelo = modelo
        self.cpu = cpu
        self.ram = ram
        self.hd = hd

mi_ordenador = Ordenador('HP', 'Pavilion', 'Ryzen 4000 Series', 16, 256)

cpu = mi_ordenador.cpu
print(cpu)
cpu = getattr(mi_ordenador, 'cpu')
print(cpu)

# gpu = mi_ordenador.gpu # AttributeError
gpu = getattr(mi_ordenador, 'gpu', 'Integrada')
print(gpu)

# mi_ordenador.gpu = 'GEFORCE GTX'
setattr(mi_ordenador, 'gpu', 'GEFORCE GTX')
print(mi_ordenador.__dict__) # {'marca': 'HP', 'modelo': 'Pavilion', 'cpu': 'Ryzen 4000 Series', 'ram': 16, 'hd': 256, 'gpu': 'GEFORCE GTX'}
