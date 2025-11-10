#pip install reportlab
"""
Crear un sistema Orientado a Objetos que a partir de una lista de invitados
genere las invitaciones en PDF y las envíe por correo electrónico.

La información de cada invitado es la siguiente:
- Nombre
- Dirección de correo
- Número de teléfono

La información de cada invitación es la siguiente:
- Nombre del invitado (podría ser una instancia de Invitado)
- Nombre del evento 
- Dirección del evento
- Fecha del evento
- Hora del evento
"""
from reportlab.pdfgen.canvas import Canvas

class Invitado:
    def __init__(self, nombre, email, telefono):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

class Invitacion:
    def __init__(self, invitado : Invitado, nombre_evento, direccion_evento, fecha_evento, hora_evento):
        self.invitado = invitado
        self.nombre_evento = nombre_evento
        self.direccion_evento = direccion_evento
        self.fecha_evento = fecha_evento
        self.hora_evento = hora_evento
    def generar_pdf(self):
        print('Generando pdf...')
        canvas = Canvas(f'{self.invitado.nombre.lower().replace(' ','_')}.pdf')
        canvas.drawString(10, 800, f'Estás invitado al evento {self.nombre_evento}...')
        canvas.drawString(10, 780, f'Fecha:{self.fecha_evento}')
        canvas.save()

class CorreoElectronicoManager:
    # Un método estático es propio de la clase, no de los objetos
    # No recibe self como primer argumento(ni cls)
    # Se le invoca poniendo el nombre de la clase seguido del método: CorreoElectronicoManager.enviar_invitacion(invitado_1)
    @staticmethod
    def enviar_invitacion(invitado : Invitado):
        # Leer el fichero con la invitación
        nombre_fichero = invitado.nombre.lower().replace(' ', '_') + '.pdf'
        print(f'Leyendo el fichero {nombre_fichero}')
        # Enviar por correo la invitación al invitado
        print(f'Enviando el fichero a {invitado.email}')

invitado_1 = Invitado('Susana López', 'susana@gmail.com', '630881100')
invitacion_1 = Invitacion(invitado_1, 'Fiesta fin de curso', 'Calle Mayor, 6, Vigo', '2025-11-28', '22:00')
invitado_2 = Invitado('Óscar Martínez', 'oscar@gmail.com', '630881100')
invitacion_2 = Invitacion(invitado_2, 'Fiesta fin de curso', 'Calle Mayor, 6, Vigo', '2025-11-28', '22:00')
invitado_3 = Invitado('Felipe Mayor', 'felipe@gmail.com', '630881100')
invitacion_3 = Invitacion(invitado_3, 'Fiesta fin de curso', 'Calle Mayor, 6, Vigo', '2025-11-28', '22:00')

invitados = [invitado_1, invitado_2, invitado_3]
invitaciones = [invitacion_1, invitacion_2, invitacion_3]

for invitacion in invitaciones:
    invitacion.generar_pdf()

for invitado in invitados:
    CorreoElectronicoManager.enviar_invitacion(invitado)