class Pelicula:
    def __init__(self, titulo, elenco):
        self.__contador = -1
        self.titulo = titulo
        self.elenco = elenco

    # Devuelve el objeto que implementa el método __next__
    def __iter__(self):
        return self
    
    # Proporciona el siguiente de cada iteracción
    def __next__(self):
        self.__contador+=1
        if (self.__contador==len(self.elenco)):
            self.__contador = -1
            raise StopIteration()
        return self.elenco[self.__contador]

pelicula = Pelicula('Match Point', ['Scarlet Johanson', 'Brad Pitt', 'Silvester Stalone', 'Al Pacino'])

for item in pelicula:
    print(item)

for item in pelicula:
    print(item)