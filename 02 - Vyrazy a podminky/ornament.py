from turtle import forward, left, exitonclick

delka_strany = 10

left(90)
forward(delka_strany/2)

while delka_strany < 200:
    delka_strany += 10
    forward(delka_strany)
    left(90)

exitonclick()
