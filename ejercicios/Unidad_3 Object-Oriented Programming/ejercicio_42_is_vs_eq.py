"""
Interning --> Técnica de optimización. Hace que distintas variables que tengan el mismo contenido
apunten a una misma zona de memoria. 
"""

nombre = 'Python'
lenguaje = 'Python'
print(nombre==lenguaje) # True, compara contenido
print(nombre is lenguaje) # True, utiliza interning

"""
Algunas técnicas de construcción de cadenas generan resultados diferentes:
"""

nombre = 'Python'
#lenguaje = 'Pithon'.replace('i','y')
lenguaje = 'python'.title()
print(nombre==lenguaje) # True, compara contenido
print(nombre is lenguaje) # False, replace o title no utilizan interning

"""
Conclusión --> COMPARAR LAS CADENAS CON == ya que el operador is puede dar "falsos positivos"
"""