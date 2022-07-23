import turtle

wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("red")
alex.shape("turtle")
alex.up()
distant = 5

for _ in range(30):
    alex.stamp()
    alex.forward(distant)
    alex.right(24)
    distant = distant + 2


wn.exitonclick()