"""
Clase Animal
- Atributos: nombre
- Métodos: comer; reproducirse

Clase Mamífero (hereda de Animal):
- Atributos: numero_dias_gestacion
- Métodos: amamantarse

Clase Perro (hereda de Mamífero):
- Atributos: raza
- Métodos: ladrar y comer

Clase Gato (hereda de Mamífero):
- Atributo: tiene_pelo (True o False)
- Métodos: maullar

Todos los métodos escriben quien hace qué: 'Soy Pluto y estoy comiendo como Perro'

- Crear las clases
- Instanciar un perro, decirle que ladre, que coma, que se amamante y que se reproduzca
- Instanciar un gato, decirle que maulle, que coma, que se amamante y que se reproduzca

NOTA: MRO - Method Resolution Order - Método de resolución de orden --> Es el conjunto de
reglas que determinan qué método se debe ejecutar cuando hay herencia.
"""
class Animal:
    def __init__(self, nombre):
        print('__init__ de Animal')
        self.nombre = nombre
    def comer(self):
        print(f'Soy {self.nombre} y estoy comiendo como Animal')
    def reproducirse(self):
        print(f'Soy {self.nombre} y me estoy reproduciendo como Animal')

class Mamifero(Animal):
    def __init__(self, nombre, numero_dias_gestacion):
        print('__init__ de Mamifero')
        super().__init__(nombre)
        self.numero_dias_gestacion = numero_dias_gestacion
    def amamantarse(self):
        print(f'Soy {self.nombre} y estoy amamantándome como Mamifero')

class Perro(Mamifero):
    def __init__(self, nombre, numero_dias_gestacion, raza):
        print('__init__ de Perro')
        super().__init__(nombre, numero_dias_gestacion)
        self.raza = raza
    def ladrar(self):
        print(f'Soy {self.nombre} y estoy ladrando como Perro')
    def comer(self):
        super().comer() # Indica que quiere ejecutar el método comer de su superclase
        print(f'Soy {self.nombre} y estoy comiendo como Perro')
    
class Gato(Mamifero):
    def __init__(self, nombre, numero_dias_gestacion, tiene_pelo : bool):
        print('__init__ de Gato')
        super().__init__(nombre, numero_dias_gestacion)
        self.tiene_pelo = tiene_pelo
    def maullar(self):
        print(f'Soy {self.nombre} y estoy maullando como Gato')

scooby_doo = Perro('Scooby Doo', 180, 'Dogo')
scooby_doo.ladrar()
scooby_doo.comer()
scooby_doo.amamantarse()
scooby_doo.reproducirse()

garfield = Gato('Garfield', 120, True)
garfield.maullar()
garfield.comer()
garfield.amamantarse()
garfield.reproducirse()

print(isinstance(garfield, Gato)) # True
print(isinstance(garfield, Perro)) # False
print(isinstance(garfield, Mamifero)) # True 
print(isinstance(garfield, Animal)) # True