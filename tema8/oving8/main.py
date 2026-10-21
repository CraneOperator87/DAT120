import turtle
import math

def tegn_kvadrat(turtle_pen, storrelse, vinkel, farger):
    """Tegn ett rotert kvadrat med en farge på hver side."""
    hjornene = []

    for side in range(4):
        hjorn_vinkel = vinkel + math.radians(45 + side * 90)
        x = storrelse / math.sqrt(2) * math.cos(hjorn_vinkel)
        y = storrelse / math.sqrt(2) * math.sin(hjorn_vinkel)
        hjornene.append((x, y))

    for side in range(4):
        turtle_pen.penup()
        turtle_pen.goto(hjornene[side])
        turtle_pen.pendown()
        turtle_pen.pencolor(farger[side])
        turtle_pen.goto(hjornene[(side + 1) % 4])


skjerm = turtle.Screen()
skjerm.bgcolor("black")
skjerm.title("Turtle-spiralmønster")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

farger = ["pink", "purple", "pink", "white", "pink", "purple", "pink", "white"]

for nummer in range(50):
    storrelse = 2 + nummer * 8
    vinkel = math.radians(nummer * 13)
    tegn_kvadrat(t, storrelse, vinkel, farger)

turtle.done()
