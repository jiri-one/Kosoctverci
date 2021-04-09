from turtle import forward, left, exitonclick

velikost = 30

while True:
    uhly = input("Zadej celým číslem počet úhlů: ")
    try:
        uhly = int(uhly)
    except:
        pass
    if str(type(uhly)) == "<class 'int'>":
        break
    
for _ in range(uhly):
    forward(velikost)
    left((2 / uhly) * 180)

exitonclick()
