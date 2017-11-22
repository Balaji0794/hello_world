import turtle

flag=turtle.Turtle()


flag.speed(0)


flag.color("#ff9933")
flag.begin_fill()
flag.forward(300)
flag.left(90)
flag.forward(50)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(50)
flag.end_fill()

flag.forward(100)

flag.color("#008000")
flag.begin_fill()
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(50)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(50)
flag.end_fill()

flag.backward(100)

flag.right(90)
flag.backward(150)
#chakra
flag.pencolor("#000080")
flag.circle(25)
flag.left(90)
flag.forward(25)

for i in range(24):
    flag.right(15)
    flag.forward(25)
    flag.backward(25)
    

flag.forward(25)
flag.left(90)
flag.forward(150)
flag.left(90)
flag.forward(50)

#border
flag.pencolor("black")
flag.forward(50)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(150)
flag.left(90)
flag.forward(300)
flag.left(90)
flag.forward(50)

flag.left(90)
flag.forward(300)
flag.right(90)
flag.forward(50)
flag.right(90)
flag.forward(300)
flag.right(90)
flag.forward(50)

flag.hideturtle()


