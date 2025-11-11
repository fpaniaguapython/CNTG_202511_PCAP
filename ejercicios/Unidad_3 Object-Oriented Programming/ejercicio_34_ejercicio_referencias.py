"""
Clase Pelicula:
- Atributos: título y director

Clase GeneradorPDFs
- Método generar(pelicula : Pelicula) --> Escribiendo en un pdf el título tal y el director cual

Instanciar varias películas, guardarlas en una lista con el método append
'Generar un pdf' de cada película.
"""
class Pelicula:
    def __init__(self, titulo, director):
        self.titulo = titulo
        self.director = director

class GeneradorPDFs:
    def generar(self, pelicula : Pelicula):
        print(f'Escribiendo un PDF con el título {pelicula.titulo} y el director {pelicula.director}')

peli_1 = Pelicula('Título 1', 'Director 1')
peli_2 = Pelicula('Título 2', 'Director 2')
peli_3 = Pelicula('Título 3', 'Director 3')

lista_peliculas = list()
lista_peliculas.append(peli_1)
lista_peliculas.append(peli_2)
lista_peliculas.append(peli_3)

generador_pdf = GeneradorPDFs()
for pelicula in lista_peliculas:
    generador_pdf.generar(pelicula)