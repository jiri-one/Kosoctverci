from turtle import forward, left, exitonclick


delka_strany = 1

left(90)
forward(delka_strany/2)

for i in range(100):
    delka_strany += 1
    forward(delka_strany)
    left((2 / 8) * 180)

exitonclick()
