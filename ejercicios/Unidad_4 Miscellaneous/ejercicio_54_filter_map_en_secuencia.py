class ProductoEntretenimiento:
    def __init__(self, titulo, euros_recaudados):
        self.titulo = titulo
        self.euros_recaudados = euros_recaudados

    def __repr__(self):
        return f'{self.titulo}:{self.euros_recaudados}'

class Pelicula:
    def __init__(self, titulo, genero, anyo, dolares_recaudados):
        self.titulo = titulo
        self.genero = genero
        self.anyo = anyo
        self.dolares_recaudados = dolares_recaudados

    def __repr__(self):
        return self.titulo

p1 = Pelicula('Rambo', 'Acción', 2008, 200_000)
p2 = Pelicula('El resplandor', 'Terror', 1988, 100_000)
p3 = Pelicula('Arma letal', 'Acción', 2001, 300_000)
p4 = Pelicula('Tiburón', 'Terror', 2024, 50_000)
p5 = Pelicula('Nothing Hill', 'Romántica', 1999, 50_000)

peliculas = [p1, p2, p3, p4, p5]

"""
Utilizando filter, map y lambdas.
Crear una lista con las películas cuyo género sea el que introduzca el usuario.
La lista estará compuesta por objetos de la clase ProductoEntrenimiento.
"""

genero = input('Introduce género:')

COTIZACION_DOLAR_EURO = 0.86

# VERSIÓN COMPACTA
#rdo = map(lambda pelicula : ProductoEntretenimiento(pelicula.titulo, pelicula.dolares_recaudados*COTIZACION_DOLAR_EURO),
#          filter(lambda pelicula : pelicula.genero==genero, peliculas))
#print(list(rdo))

# VERSIÓN 'EXTENDIDA'
peliculas_genero = filter(lambda pelicula : pelicula.genero==genero, peliculas)
productos_entretenimiento = map(lambda pelicula : ProductoEntretenimiento(pelicula.titulo, pelicula.dolares_recaudados*COTIZACION_DOLAR_EURO), peliculas_genero)
print(list(productos_entretenimiento))