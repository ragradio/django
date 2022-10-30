 # ##########################################
 
class Lobo(object):
    """ Clase Lobo  """
    def __init__(self, nombre, genero, especie, clan):
        """Constructor/inicializador de Lobo"""
        self.nombre = nombre
        self.genero = genero
        self.especie = especie
        self.clan = clan

    def __str__(self):
        return " %s: %s, %s %s" % (str(self.nombre), self.genero,self.especie,self.clan)

if __name__ == '__main__':
    lobo1= Lobo('amparo','común','hembra','páramo');
    print(lobo1)
