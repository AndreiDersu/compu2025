from math import *

def cuadratic_formula (a=int, b=int, c=int):
    """Sean a,b,c numeros reales tal que ax**2+bx+c=0, con a distinto a 0.
    Se admiten resultados complejos."""
    if a != 0:
        dis = b ** 2 - 4 * a * c
        
        x1 = -b + dis ** (1/2) / (2 * a)
        
        x2 = -b - dis ** (1/2) / (2 * a)
        
        x=[x1,x2]
        print(x1,x2)
        return (x)
    else:
        pass