"""
Relación de herencia
En la subclase (clase derivada) se indica entre paréntesis la superclase (clase base)
super() hace referencia a la 'versión' de la superclase de aquello a lo que se invoca
El constructor de la subclase 'normalmente' debe invocar al constructor de la superclase
"""

class Persona:
    def __init__(self, nombre, fecha_nacimiento):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.energia = 100 # El valor inicial no se recibe como argumento de __init__

    def comer(self, energia_extra):
        self.energia+=energia_extra

    def dormir(self, numero_horas):
        self.energia+=numero_horas*10

class Programador(Persona): # Programador hereda (extiende a) de persona
    def __init__(self, nombre, fecha_nacimiento, lenguaje):
        super().__init__(nombre, fecha_nacimiento)
        self.lenguaje = lenguaje
        
lara = Programador('Lara', '1995', 'Python')
print(lara.nombre)
print(lara.energia)
print(lara.lenguaje)

# A continuación se muestra la evidencia de que un objeto Programador es polimórfico 
print(isinstance(lara, Programador)) # True
print(isinstance(lara, Persona)) # True

