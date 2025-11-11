class Baliza:
    geolocalizacion_obligatoria = False # Atributo de clase
    def __init__(self, marca, duracion_bateria, pvp):
        self.marca = marca # Atributo de instancia
        self.duracion_bateria = duracion_bateria # Atributo de instancia
        self.pvp = pvp # Atributo de instancia
    def mostrar_info(self):
        pass

baliza_1 = Baliza('Ledone', 2.5, 37.99)
baliza_2 = Baliza('Raypow', 3.0, 35.00)

print(baliza_1.__dict__) # Atributos de instancia: {'marca': 'Ledone', 'duracion_bateria': 2.5, 'pvp': 37.99} 
print(baliza_2.__dict__) # Atributos de instancia: {'marca': 'Raypow', 'duracion_bateria': 3.0, 'pvp': 35.0}

print(Baliza.geolocalizacion_obligatoria) # False. Es un atributo de clase
Baliza.geolocalizacion_obligatoria = True # Cambiamos el valor
print(Baliza.geolocalizacion_obligatoria) # True. Es un atributo de clase

print(baliza_1.geolocalizacion_obligatoria) # True (NO USAR)
baliza_1.geolocalizacion_obligatoria = False # Crea un nuevo atributo de instancia (NO USAR)
print(baliza_1.__dict__) # {'marca': 'Ledone', 'duracion_bateria': 2.5, 'pvp': 37.99, 'geolocalizacion_obligatoria': False}

print(Baliza.__dict__) # Muestra los atributos de clase (incluye los métodos):
# {
# '__module__': '__main__', 
# '__firstlineno__': 1, 
# 'geolocalizacion_obligatoria': True, 
# '__init__': <function Baliza.__init__ at 0x000001F8867A35E0>, 
# 'mostrar_info': <function Baliza.mostrar_info at 0x000001F8867A3690>, 
# '__static_attributes__': ('duracion_bateria', 'marca', 'pvp'), 
# '__dict__': <attribute '__dict__' of 'Baliza' objects>, 
# '__weakref__': <attribute '__weakref__' of 'Baliza' objects>, 
# '__doc__': None
# }