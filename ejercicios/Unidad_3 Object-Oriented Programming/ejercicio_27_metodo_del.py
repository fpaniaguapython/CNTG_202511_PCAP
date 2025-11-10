class Pelicula:
    # Se ejecuta despues del crear el objeto
    def __init__(self, titulo):
        self.titulo = titulo
        print(f'Inicializador: {self.titulo}')

    # Se ejecuta antes de destruir el objeto
    def __del__(self):
        print(f'Finalizador: {self.titulo}')

def gestionar_pelicula():
    pelicula_local = Pelicula('Spiderman')
    print('Fin de la función gestionar_pelicula')

pelicula_global = Pelicula('Batman')
pelicula_global = None
gestionar_pelicula()
print('Fin de la ejecución')