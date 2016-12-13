import turtle               # allows us to use the turtles library

window = turtle.Screen()        # creates a graphics window

elise = turtle.Turtle()      # create a turtle named elies
elise.forward(50)           # tell nick to move forward by 150 units
elise.left(90)               # turn by 90 degrees
elise.forward(50)            # complete the second side of a rectangle
elise.left(90)
elise.forward(50)
elise.left(90)
elise.forward(50)
window.exitonclick()
