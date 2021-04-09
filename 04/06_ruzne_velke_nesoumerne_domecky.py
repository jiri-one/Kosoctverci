from math import sqrt, cos, radians, degrees, atan
from turtle import forward, left, right, exitonclick, pendown, penup

def nakresli_baracek(vodorovna, svisla):
    vnitrni_uhel = degrees(atan(svisla/vodorovna))
    for obdelnik in range(2):
        forward(vodorovna)
        left(90)
        forward(svisla)
        left(90)

    left(vnitrni_uhel)
    forward(sqrt(vodorovna ** 2 + svisla ** 2))

    left(90-vnitrni_uhel+45) # Střecha
    forward(vodorovna/2 / cos(radians(45)))
    left(90)
    forward(vodorovna/2 / cos(radians(45)))

    left(90-vnitrni_uhel+45)
    forward(sqrt(vodorovna ** 2 + svisla ** 2))
    left(vnitrni_uhel)

    penup()
    forward(20)
    pendown()

nakresli_baracek(30, 50)
nakresli_baracek(50, 20)
nakresli_baracek(100, 150)
exitonclick()
