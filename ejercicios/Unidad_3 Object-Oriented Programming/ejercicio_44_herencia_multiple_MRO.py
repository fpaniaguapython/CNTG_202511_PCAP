class Automovil:
    def __init__(self, nombre):
        print('(Automóvil) Constructor...')
        self.nombre = nombre
        self.km_hora_maximos = 120
    def arrancar(self):
        print('(Automóvil) Arrancando...')
    def parar(self):
        print('(Automóvil) Parando...')
    def circular(self):
        print('(Automóvil) Circulando...')

class Barco:
    def __init__(self, nombre):
        print('(Barco) Constructor...')
        self.nombre = nombre
        self.nudos_maximos = 20
    def arrancar(self):
        print('(Barco) Arrancando...')
    def parar(self):
        print('(Barco) Parando...')
    def navegar(self):
        print('(Barco) Navegando...')

class Anfibio(Automovil, Barco):
    def __init__(self, nombre):
        # ATENCIÓN: Tenemos que llamar a los dos constructores de las clases base explícitamente
        # Si hacemos super().__init__ se va a la primera clase de la herencia (en este caso Automovil)
        Automovil.__init__(self, nombre) 
        Barco.__init__(self, nombre)
        self.profundidad_minima = 10
    def arrancar(self):
        print('(Anfibio) Arrancando...')

aerodeslizador = Anfibio('Batmovil') # (Automóvil) Constructor...
aerodeslizador.arrancar() # (Anfibio) Arrancando...
aerodeslizador.parar() # (Automóvil) Parando...
aerodeslizador.navegar() # (Barco) Navegando...
aerodeslizador.circular() # (Automóvil) Circulando...

print(aerodeslizador.__dict__) # Incluye los atributos de instancia de todas las clases