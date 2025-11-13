class Pelicula:
    def __init__(self, titulo, genero, anyo, dolares_recaudados):
        self.titulo = titulo
        self.genero = genero
        self.anyo = anyo
        self.dolares_recaudados = dolares_recaudados

    def __repr__(self):
        return f'{self.titulo}:{self.genero}'
    

p1 = Pelicula('Rambo', 'Acción', 2008, 200_000)
p2 = Pelicula('El resplandor', 'Terror', 1988, 100_000)
p3 = Pelicula('Arma letal', 'Acción', 2001, 8_000)
p4 = Pelicula('Tiburón', 'Terror', 2024, 75_000)
p5 = Pelicula('Nothing Hill', 'Romántica', 1999, 50_000)

peliculas = [p1, p2, p3, p4, p5]

# Comprensión de listas simple
todos_los_titulos = [pelicula.titulo for pelicula in peliculas]
print(todos_los_titulos) # ['Rambo', 'El resplandor', 'Arma letal', 'Tiburón', 'Nothing Hill']

# Comprensión de listas con if
titulos_peliculas_terror = [pelicula.titulo for pelicula in peliculas if pelicula.genero=='Terror']
print(titulos_peliculas_terror) # ['El resplandor', 'Tiburón']

# Comprensión de listas con if-else
todas_las_peliculas = [pelicula if pelicula.genero=='Terror' else 'Película no interesante' for pelicula in peliculas]
print(todas_las_peliculas) # ['Película no interesante', El resplandor:Terror, 'Película no interesante', Tiburón:Terror, 'Película no interesante'] 