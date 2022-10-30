class Figura(object):
    """ Una figura en el plano. """
    def area(self):
        " Este método debe ser redefinido. "
        pass

from math import pi

class Circulo(Figura):
    """ Un círculo en el plano. """
    def __init__(self, radio=0):
        " Constructor de círculo. "
        self.radio = radio

    def area(self):
        " Devuelve el área del círculo. "
        return pi * self.radio * self.radio

class Triangulo(Figura):
    """ Un triángulo en el plano. """
    def __init__(self, base=0, altura=0):
        " Constructor de triángulo. "
        self.base = base
        self.altura = altura

    def area(self):
        " Devuelve el área del triángulo. "
        return self.base * self.altura / 2.

################################

c = Circulo(4)
print("Area Circulo:",c.area())
t = Triangulo(3, 5)
print("Area Triangulo:",t.area())
