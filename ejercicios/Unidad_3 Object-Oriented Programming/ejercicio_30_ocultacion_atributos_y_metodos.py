class Empleado:
    def __init__(self, nombre : str, categoria : str, salario : int):
        self.nombre = nombre
        self.categoria = categoria
        self.__salario = salario # Es un atributo privado (permite encapsular)

    def __verificar_salario(self): # Este método se 'enmascara'
        print('Verificando salario...')

    # Getter (encapsulación)
    def get_salario(self):
        return self.__salario
    
    # Setter (encapsulación)
    def set_salario(self, nuevo_salario):
        self.__salario = nuevo_salario

fernando = Empleado('Fernando', 'Profesor', 15_000)
print(fernando.nombre)
print(fernando.categoria)
# print(fernando.__salario) # Error
print('Salario:', fernando._Empleado__salario) # Es la sustitución de __salario - NO USAR
print('Salario:', fernando.get_salario()) # Permite el acceso de lectura - SÍ USAR

# fernando.__verificar_salario() # Error
fernando._Empleado__verificar_salario() # Es la sustitución de __verificar_salario - NO USAR

print(fernando.__dict__) # {'nombre': 'Fernando', 'categoria': 'Profesor', '_Empleado__salario': 15000}