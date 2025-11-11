#
# Herencia
#
class Enemigo:
    def __init__(self, nombre, energia):
        self.nombre = nombre 
        self.energia = energia
        self.posicion = [0,0,0]

    def desplazar(self, vector_desplazamiento : list):
        self.posicion[0]+=vector_desplazamiento[0]
        self.posicion[1]+=vector_desplazamiento[1]
        self.posicion[2]+=vector_desplazamiento[2]

class EnemigoAgresivo(Enemigo):
    def atacar(self):
        print('Atacando...')

#
# Composición
#
class Enemigo:
    def __init__(self, nombre, energia, arma=None):
        self.nombre = nombre 
        self.energia = energia
        self.posicion = [0,0,0]
        self.arma=arma # Una referencia a un objeto que se ha creado

    def desplazar(self, vector_desplazamiento : list):
        self.posicion[0]+=vector_desplazamiento[0]
        self.posicion[1]+=vector_desplazamiento[1]
        self.posicion[2]+=vector_desplazamiento[2]

    def atacar(self):
        if self.arma:
            self.arma.disparar()

class Arco:
    def __init__(self):
        self.nombre = 'Arco'
    def disparar(self):
        print('Estoy disparando como Arco')


arco = Arco()
saruman = Enemigo('Saruman', 100, arco)
piolin = Enemigo('Piolín', 50)

saruman.atacar()
piolin.atacar()