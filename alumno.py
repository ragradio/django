class Persona(object):
    "Clase que representa una persona."
    def __init__(self, identificacion, nombre, apellido):
        "Constructor/inicializador de Persona"
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return " %s: %s, %s" % (str(self.identificacion), self.apellido, self.nombre)


class Alumno(Persona):
    "Clase que representa a un alumno de UniZar"
    def __init__(self, identificacion, nombre, apellido, nip):
        "Constructor de Alumno"
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombre, apellido)
        # agregamos el nuevo atributo
        self.nip = nip

#--------------------------------

#a = Alumno("DNI 35123456", "Damien", "Thorn", "98765")
#print (a)


