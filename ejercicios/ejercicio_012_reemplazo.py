ficheros = ['image001.jpg', 'documento.pdf', 'image002.jpg', 'image003.JPG']

# Crear una lista con los nombres de los ficheros de imágenes
# eliminado las extensiones .jpg utilizando slicing

posicion = 'prueba.jpg'.find('.jpg')
print(posicion) # 6
posicion = 'prueba.jpg'.find('.bmp')
print(posicion) # -1

# Opción 1
nombres = list()
for fichero in ficheros:
    posicion = fichero.lower().find('.jpg')
    if posicion != -1:
        nombre = fichero[:posicion]
        nombres.append(nombre)
print(nombres) # ['image001', 'image002', 'image003']

# Opción 2 (con comprensión de listas)
nombres = [(fichero[:fichero.lower().find('.jpg')]) for fichero in ficheros if (fichero.lower().find('.jpg')!=-1)]
print(nombres)

# Opción Damián (con compresión de listas)
nombres = [f[:-4] for f in ficheros if f.lower().endswith(('.jpg'))]
print(nombres)