import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(1080,1920)
sides = 6
pen = turtle.Turtle()
for i in range(sides):
    pen.forward(100)
    pen.right(60)

turtle.done()