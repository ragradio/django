class Mascota(object):
    def __init__(self,nombre,especie):
       """
       Inicializador de mascota
       """
       self.nombre=nombre
       self.especie=especie

    def nombre(self):
      """
      devolvemos el nombre
      """
      return self.nombre

    def especie(self):
       """
       devolvemos la especie
       """
       return self.especie

    def __str__(self):
       """
       print invoca el metodo __str__
       """
       return "me llamon %s de la especie %s" %(self.nombre,self.especie)


p1=Mascota('sultan','perro')
print(p1.nombre)
print(p1.especie)
print (p1)
p1.nombre="rayo"
p1.especie="gato"
print(p1.nombre)
print(p1.especie)
print (p1)
