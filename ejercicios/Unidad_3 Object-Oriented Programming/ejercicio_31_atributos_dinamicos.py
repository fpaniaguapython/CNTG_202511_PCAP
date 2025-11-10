class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

    def agregar_anyo(self, anyo):
        self.anyo = anyo

el_resplandor = Pelicula('El Resplandor', 'Kubrick')
alien = Pelicula('Alien', 'Ridley')
alien.agregar_anyo(1988)

print(el_resplandor.__dict__) # {'titulo': 'El Resplandor', 'director': 'Kubrick'}
print(alien.__dict__) # {'titulo': 'Alien', 'director': 'Ridley', 'anyo': 1988}

# Quiero cambiar el valor del atributo director pero cometo un error tipográfico
el_resplandor.directo = 'John Rambo'
# PROBLEMÓN --> El error tipográfico ha creado un nuevo atributo que no era lo que queríamos hacer
print(el_resplandor.__dict__) # {'titulo': 'El Resplandor', 'director': 'Kubrick', 'directo': 'John Rambo'}