import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

elise = turtle.Turtle()      # create a turtle named elies
elise.forward(70)           # tell nick to move forward by 150 units
elise.left(90)               # turn by 90 degrees
elise.forward(70)            # complete the second side of a rectangle
elise.left(90)
elise.forward(70)
elise.left(90)
elise.forward(70)
elise.penup(3)
elise.pendown(3)
elise.left(20)
elise.forward(70)           # tell nick to move forward by 150 units
elise.left(90)               # turn by 90 degrees
elise.forward(70)            # complete the second side of a rectangle
elise.left(90)
elise.forward(70)
elise.left(90)
elise.forward(70)

window.exitonclick()
