from turtle import right, left, forward, exitonclick, speed

def stromecek(delka, uhel):
	if delka < 20:
		for _ in range(2):
			forward(delka)
			right(180)
	else:
		forward(delka/2)
		right(uhel)
		stromecek(delka/2, uhel*2/3)
		left(uhel)
		stromecek(delka/2, uhel*2/3)
		left(uhel)
		stromecek(delka/2, uhel*2/3)
		right(uhel+180)
		forward(delka/2)
		right(180)

speed(10)
left(90)
stromecek(200, 60)
exitonclick()
		