class Pelicula:
    def __init__(self, titulo, genero, anyo, dolares_recaudados):
        self.titulo = titulo
        self.genero = genero
        self.anyo = anyo
        self.dolares_recaudados = dolares_recaudados

    def __repr__(self):
        return self.titulo
    
    def __lt__(self, other : Pelicula):
        return self.anyo < other.anyo


p1 = Pelicula('Rambo', 'Acción', 2008, 200_000)
p2 = Pelicula('El resplandor', 'Terror', 1988, 100_000)
p3 = Pelicula('Arma letal', 'Acción', 2001, 8_000)
p4 = Pelicula('Tiburón', 'Terror', 2024, 75_000)
p5 = Pelicula('Nothing Hill', 'Romántica', 1999, 50_000)

peliculas = [p1, p2, p3, p4, p5]

# sorted(peliculas) --> Función --> NO modifica peliculas
peliculas_ordenadas_con_lt = sorted(peliculas)
print(peliculas_ordenadas_con_lt) # [El resplandor, Nothing Hill, Arma letal, Rambo, Tiburón]
print(peliculas) # [Rambo, El resplandor, Arma letal, Tiburón, Nothing Hill]

# peliculas.sort()  --> Método -->  SÍ modifica peliculas
peliculas.sort()
print(peliculas) # [El resplandor, Nothing Hill, Arma letal, Rambo, Tiburón]

# Argumento key (aplicaría igual a sorted)

def valoracion_por_recaudacion(pelicula : Pelicula):
    return pelicula.dolares_recaudados

def valoracion_por_anyo(pelicula : Pelicula):
    return pelicula.anyo

peliculas.sort(key=valoracion_por_anyo, reverse=True)
print(peliculas)

# Ejercicio: Ordenar mediante lambdas por Título, Género, Recaudación y Año
# Atención 👁️👁️: No debe influir que los textos estén mayúsculas o minúsculas

peliculas.sort(key=lambda pelicula: pelicula.titulo.lower())
print("Ordenación por título:", peliculas) # Ordenación por título: [Arma letal, El resplandor, Nothing Hill, Rambo, Tiburón]

peliculas.sort(key=lambda pelicula: pelicula.genero.lower())
print("Ordenación por género:", peliculas) # Ordenación por género: [Arma letal, Rambo, Nothing Hill, El resplandor, Tiburón]

peliculas.sort(key=lambda pelicula: pelicula.dolares_recaudados)
print("Ordenación por recaudación:", peliculas) # Ordenación por recaudación: [Arma letal, Nothing Hill, Tiburón, El resplandor, Rambo]

peliculas.sort(key=lambda pelicula: pelicula.anyo)
print("Ordenación por año:", peliculas) # Ordenación por año: [El resplandor, Nothing Hill, Arma letal, Rambo, Tiburón]