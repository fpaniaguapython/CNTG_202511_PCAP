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
from reportlab.lib.units import mm

class Invitado:
    def __init__(self, nombre : str, email : str, telefono : str):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

class Evento:
    def __init__(self, nombre : str, direccion : str, fecha : str, hora : str, logotipo=None):
        self.nombre = nombre
        self.direccion = direccion
        self.fecha = fecha
        self.hora = hora
        self.logotipo = logotipo

class Invitacion:
    def __init__(self, evento : Evento, invitado : Invitado):
        self.evento = evento
        self.invitado = invitado

    def get_pdf(self) -> bytes:
        print('Generando pdf...')
        width, height = 85 * mm, 55 * mm
        nombre_fichero = f'{self.invitado.nombre.lower().replace(' ','_')}.pdf'
        canvas = Canvas(nombre_fichero, pagesize=(width, height))
        canvas.setFont('Courier', 18)
        canvas.drawCentredString(120, 100, f'¡{self.evento.nombre}!')
        canvas.setFontSize(15)
        canvas.drawCentredString(120, 80, self.invitado.nombre)
        canvas.setFontSize(5)
        canvas.drawString(5, 20, f'Dónde:  {self.evento.direccion}')
        canvas.drawString(5, 12, f'Cuándo: {self.evento.fecha}-{self.evento.hora}')
        if self.evento.logotipo:
            canvas.drawImage(self.evento.logotipo, x=100, y=30, width=40, height=40, preserveAspectRatio=True, mask='auto')
        canvas.save()
        pdf_data = canvas.getpdfdata() # Devuelve un objeto de la clase bytes
        return pdf_data 

class CorreoElectronicoManager:
    # Un método estático es propio de la clase, no de los objetos
    # No recibe self como primer argumento(ni cls)
    # Se le invoca poniendo el nombre de la clase seguido del método: CorreoElectronicoManager.enviar_invitacion(invitado_1)
    @staticmethod
    def enviar_invitacion(invitado : Invitado, pdf_invitacion : bytes):
        # Enviar por correo la invitación al invitado
        print(f'Enviando invitación a {invitado.email}')

fiesta_jaloguin = Evento(
    nombre='Fiesta de Jaloguin', 
    direccion='La Tita. Rúa Nova, 46, Santiago de Compostela', 
    fecha='31/10/2026', 
    hora='23:59', 
    logotipo='calabaza.png')

invitado_1 = Invitado('Susana López', 'susana@gmail.com', '630881100')
invitado_2 = Invitado('Óscar Martínez', 'oscar@gmail.com', '630881100')
invitado_3 = Invitado('Felipe Mayor', 'felipe@gmail.com', '630881100')

invitacion_1 = Invitacion(evento=fiesta_jaloguin, invitado=invitado_1)
invitacion_2 = Invitacion(evento=fiesta_jaloguin, invitado=invitado_2)
invitacion_3 = Invitacion(evento=fiesta_jaloguin, invitado=invitado_3)

invitaciones = [invitacion_1, invitacion_2, invitacion_3]

for invitacion in invitaciones:
    pdf_invitacion = invitacion.get_pdf()
    CorreoElectronicoManager.enviar_invitacion(invitado=invitacion.invitado, pdf_invitacion=pdf_invitacion)