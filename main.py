import turtle


def escalier(taille, nb_marche):
    for i in range(nb_marche):
        t.forward(taille)
        t.left(90)
        t.forward(taille)
        t.right(90)
    t.forward(taille)


def caree(taille):
    for i in range(4):
        t.forward(taille)
        t.left(90)


def carees(taille_depart, nb_caree):
    for i in range(nb_caree):
        taille = (i+1) * taille_depart
        caree(taille)

t = turtle.Turtle()


# escalier(30, 10)
# caree(50)
carees(30, 4)

turtle.done()