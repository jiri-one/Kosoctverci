Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:57:54) [MSC v.1924 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> turtle.left(60)
>>> turtle.forward(200)
>>> turtle.left(30)
>>> turtle.left(30)
>>> turtle.forward(200)
>>> turtle.left(120)
>>> turtle.forward(200)
>>> turtle.left(60)
>>> turtle.forward(200)
>>> turtle.left(150)
>>> turtle.penup()
>>> from math import sqrt
>>> degree
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    degree
NameError: name 'degree' is not defined
>>> from math import sqrt, degree
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    from math import sqrt, degree
ImportError: cannot import name 'degree' from 'math' (unknown location)
>>> from math import sqrt, degree
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    from math import sqrt, degree
ImportError: cannot import name 'degree' from 'math' (unknown location)
>>> 