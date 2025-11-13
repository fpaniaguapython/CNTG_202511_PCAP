LOG_FILE = 0
LOG_DATABASE = 1
LOG_WEB_SERVICE = 2

def get_log_function(tipo_log : int):
    def inner_function(log):
        match tipo_log:
            case 0:
                print(f'Escribiendo a fichero {log}')
            case 1:
                print(f'Escribiendo a base de datos {log}')
            case 2:
                print(f'Escribiendo a servicio web {log}')
            case _:
                print(f'Escribiendo a consola {log}')
    return inner_function

# Obteniendo versiones con configuración de una función (inner_function)
logger_fichero = get_log_function(LOG_FILE)
logger_base_de_datos = get_log_function(LOG_DATABASE)
logger_servicio_web = get_log_function(LOG_WEB_SERVICE)

# Utilizamos las funciones con sus configuraciones correspondientes
logger_servicio_web('Intento fallido de acceso') # Escribiendo a servicio web Intento fallido de acceso
logger_base_de_datos('Acción no disponible') # Escribiendo a base de datos Acción no disponible