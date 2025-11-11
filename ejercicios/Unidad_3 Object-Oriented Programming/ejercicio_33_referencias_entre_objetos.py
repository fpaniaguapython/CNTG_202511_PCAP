class Motor:
    def arrancar(self):
        print("Arrancando...")
    def acelerar(self):
        print("Acelerando...")
    def apagar(self):
        print("Apagando...")

class Vehiculo:
    def trasladar(self, motor : Motor):
        motor.arrancar()
        motor.acelerar()
        motor.acelerar()
        motor.acelerar()
        motor.apagar()

motor_v1 = Motor()
vehiculo_v1 = Vehiculo()

vehiculo_v1.trasladar(motor_v1)