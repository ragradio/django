""" 
Modulo para el calculo de areas de formas basicas 
"""
pi = 3.1416
def cuadrado ( lado ):
    """ 
    Calcula el area del cuadrado a partir de su lado 
    """
    return lado ** 2
def circulo ( radio ): 
    """ Calcula el area del circulo dado el radio 
    """
    return pi * radio ** 2

###############################################

print (' Area cuadrado = ' , cuadrado (2))
print (' Area circulo = ', circulo (1))
