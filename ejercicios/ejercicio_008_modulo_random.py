import random

# Función random
print(random.random()) # [0,1) n>=0 n<1

# Función seed (establece la semilla)
random.seed() # Las secuencias de generación serán distintas (en función de la hora del sistema)
random.seed('Python') # A partir de aquí, todas las secuencias de generación serán iguales
print(random.random())
print(random.random())

# Función randrange 
random.seed()
for i in range(100):
    print('randrange:', random.randrange(10)) # Genera un entero entre 0 y 9 (10-1)

# Función randint
for i in range(100):
    print('randint:', random.randint(0,10)) # Genera un entero entre 0 y 10

# Función choice
lista = ['Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco']
print(random.choice(lista))


