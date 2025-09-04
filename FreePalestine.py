import turtle

# Configuration de la fenetre
ecran = turtle.Screen()
ecran.title('Free Palestine')
ecran.bgcolor('white')

t = turtle.Turtle()
t.speed(5)

# Fonction Pour dessiner un rectangle rempli
def rectangle(couleurs, x, y, largeur, hauteur):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(couleurs)
    t.begin_fill()
    for i in range(2):
        t.forward(largeur)
        t.right(90)
        t.forward(hauteur)
        t.right(90)
    t.end_fill()

# Dimenssions
largeur = 300
hauteur = 90
x_debut = -150
y_debut = 100

# Dessiner les 3 bandes horizontales
# Bande noire
rectangle('black', x_debut, y_debut, largeur, 
            hauteur/3)
# Bande blanche
rectangle('white', x_debut, y_debut - hauteur - 10, 
            largeur, hauteur/3)
# Bande verte
rectangle('green', x_debut, y_debut - 2*hauteur/3, 
            largeur, hauteur/3)

# Dessiner le triangle en rouge et centre
t.penup()
t.goto(x_debut, y_debut)
t.pendown()
t.color('red')
t.begin_fill()
t.goto(x_debut, y_debut - hauteur)
t.goto(x_debut + largeur/3, y_debut - hauteur /2)
t.goto(x_debut, y_debut)
t.end_fill()

# Ecrire Free Palestine
t.penup()
t.goto(-120, y_debut - hauteur -30)
t.color('green')
t.write('FREE PALESTINE', font=('Arial', 20, 'bold'))

t.hideturtle() # pour cacher la tortue
turtle.done()

