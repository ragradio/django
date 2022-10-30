class Punto(object):
    """ Representación de un punto en el plano, los atributos son x e y
        que representan los valores de las coordenadas cartesianas."""

    def __init__(self, x=0, y=0):
        """ Constructor de Punto, x e y deben ser numéricos,
            de no ser así, se levanta una excepción TypeError """
        if self.es_numero(x) and self.es_numero(y):
            self.x=x
            self.y=y
        else:
            raise TypeError("x e y deben ser valores numéricos")

    def es_numero(self,valor):
        """ Indica si un valor es numérico o no. """
        return isinstance(valor, (int, float, complex) )

    def distancia(self, otro):
        """ Devuelve la distancia entre ambos puntos. """
        dx = self.x - otro.x
        dy = self.y - otro.y
        return (dx*dx + dy*dy)**0.5

    def __str__(self):
        """ Muestra el punto como un par ordenado. """
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __add__(self, otro):
        """ Devuelve la suma de ambos puntos. """
        return Punto(self.x + otro.x, self.y + otro.y)

    def __sub__(self, otro):
        """ Devuelve la resta de ambos puntos. """
        return Punto(self.x - otro.x, self.y - otro.y)

##############################################

p = Punto(-6,18)
str(p)
print (p)
print(p.x)
print(p.y)

p=Punto(3,4)
q=Punto(5,9)
print(p-q)
print(p+q)
