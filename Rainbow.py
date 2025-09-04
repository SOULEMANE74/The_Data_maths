import turtle # module qui permet de dessiner 

ecran = turtle.Screen() # creation du fenetre de dessin
ecran.bgcolor("white") # fond blanc

t= turtle.Turtle()
t.speed(0)
t.width(2)

coleurs=["red","orange","yellow","green","blue","indigo","violet"]

for i in range(720):
    t.color(coleurs[i%7])
    t.forward(i*4/len(coleurs))
    t.left(120)
    t.left(1)

turtle.done()
