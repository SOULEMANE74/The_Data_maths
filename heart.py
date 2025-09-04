import math
from turtle import *
# fonctions parametriques
# coordonnees suivant ox
def coeurx(n):
    return 15*math.sin(n)**3
# coordonnees suivant oy
def coeury(n):
    return 12*math.cos(n)\
        -5*math.cos(2*n)\
        -2*math.cos(3*n)\
        -math.cos(4*n)
speed(0)
bgcolor("black")
# boucle du dessin 
for i in range(6000):
    goto(coeurx(i)*20, coeury(i)*20)
    for j in range(1):
        color("red")
    goto(0,0)
done()


