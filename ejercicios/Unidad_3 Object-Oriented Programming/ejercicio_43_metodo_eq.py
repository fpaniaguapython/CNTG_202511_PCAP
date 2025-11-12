# == -> Compara contenido
# is -> Compara identidad (que sean el mismo objeto)

class Cosa:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
    def __eq__(self, other):
        return self.color==other.color

raton = Cosa('Ratón', 'Gris Claro')
taza = Cosa('Taza', 'Gris Claro')
cable = Cosa('Cable', 'Negro')
cable_duplicado = cable

# Sin método de comparación __eq__
print('1:', raton==taza) # False
print('2:', raton is taza) # False
print('3:', cable_duplicado==cable) # True
print('4:', cable_duplicado is cable) # True

# Con método de comparación __eq__
print('5:', raton==taza) # True
print('6:', raton is taza) # False
print('7:', cable_duplicado==cable) # True
print('8:', cable_duplicado is cable) # True