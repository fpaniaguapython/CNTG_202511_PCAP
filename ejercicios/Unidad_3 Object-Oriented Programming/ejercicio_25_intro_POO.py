import time

# Clase
class EmpleadoAutorizado:
    pass

# Instanciar (crear un objeto)
maria_jesus = EmpleadoAutorizado()

# Objeto o Instancia
maria_jesus # Es un objeto o instancia

# Atributos
# Son públicos
# Se pueden crear en cualquier momento
class Empleado:
    def __init__(self, nombre : str, numero : int, fecha_contratacion : str):
        # Atributos:
        self.nombre = nombre # self.nombre es el atributo
        self.numero = numero # self.numero es el atributo
        self.fecha_contratacion = fecha_contratacion # self.fecha_contratacion es el atributo

antonio_jose = Empleado('Antonio Jose', 108, '20251109') # Instanciación de un objeto Empleado
antonio_jose.nombre = 'Antonio José' # Acceso al atributo para asignarle un valor
print(antonio_jose.nombre) # Acceso al atributo para leer su valor

# Métodos
class Automovil:
    def __init__(self, matricula, marca, modelo, color, tipo_combustible):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tipo_combustible = tipo_combustible
        print(f'Soy {self.matricula} y me acaban de crear')

    def arrancar(self, retardo : int):
        """
        Arranca el motor

        Params:
            retardo (int): Número de segundos que espera antes de arrancar
        """
        print(f'Soy {self.matricula} y estoy arrancando el motor')
        time.sleep(retardo)
        print(f'Soy {self.matricula} y he arrancado el motor')

    def parar(self):
        print(f'Soy {self.matricula} y acabo de parar el motor')

    def __del__(self):
        print(f'Soy {self.matricula} y este es mi método "destructor"')

seat_panda = Automovil('7748-KRS', 'Seat', 'Panda', 'Gris', 'Gasolina')
seat_panda.arrancar(3)
seat_panda.parar()


# ¿Constructor?
# El método mágico __init__ inicializa el objeto (constructor). 

# ¿Destructor?
# El método mágico __del__ se ejecuta cuando el objeto se 'destruye'


