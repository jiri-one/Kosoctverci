from math import sqrt, cos, radians
from turtle import forward, left, right, exitonclick, pendown, penup

def nakresli_baracek(strana):
    for ctverec in range(4):
        forward(strana)
        left(90)

    left(45)
    forward(sqrt(2) * strana)

    left(90)            # Střecha
    forward(strana/2 / cos(radians(45)))
    left(90)
    forward(strana/2 / cos(radians(45)))

    left(90)
    forward(sqrt(2) * strana)

    left(45)
    penup()
    forward(20)
    pendown()

nakresli_baracek(30)
nakresli_baracek(50)
nakresli_baracek(100)
exitonclick()
