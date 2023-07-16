import turtle
turtle.bgcolor("light pink")
turtle.pensize(2.5)
turtle.speed()
color=["red","green","blue","yellow"]
for x in range(10):
    for i in color:
        turtle.color(i)
        turtle.shape(200)
        turtle.left(10)
turtle.mainloop()
