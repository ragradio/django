
# ##########################################

from persona import Persona 
per1= Persona('3433444','roberto','curseando');
print(per1)

# ##########################################

from animales import Lobo
lobo1= Lobo('amparo','común','hembra','páramo');
print(lobo1)

# ##########################################

class Hombre_lobo(Persona,Lobo):
   """ Clase Lobo  """
   def __init__(self, identificacion, nombre, apellido, genero, especie, clan, fecha_conversion):
        """Constructor/inicializador de Lobo"""
        Persona.__init__(self,identificacion,nombre,apellido)
        Lobo.__init__(self,nombre,genero,especie,clan)
        self.fecha_conversion=fecha_conversion

   def __str__(self):
       return " %s, %s , %s " % (Persona.__str__(self), Lobo.__str__(self), self.fecha_conversion);

if __name__ == '__main__':
    hombre_lobo1= Hombre_lobo('34443223','amparo','sanchez','hembra','lobo comun','páramo','14/5/2020');
    print(hombre_lobo1)
