#
###############################################################################
#
class Persona(object):
    "Clase que representa una persona."
    def __init__(self, identificacion, nombre, apellido):
        "Constructor/inicializador de Persona"
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
        
    def __str__(self):
        return " %s: %s, %s" % (str(self.identificacion), self.apellido, self.nombre)

if __name__ == '__main__':
    per1= Persona('3433444','roberto','curseando');
    print(per1)
