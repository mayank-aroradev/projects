from turtle import Turtle , Screen

timmy_the_turtle = Turtle()
Screen = Screen() 


def move_forward():
    timmy_the_turtle.forward(10)

def move_backward():
    timmy_the_turtle.backward(10)

def move_left():
    new_heading = timmy_the_turtle.heading() + 10

def move_right():
    new_heading = timmy_the_turtle.heading() - 10 
    timmy_the_turtle.setheading(new_heading)





Screen.listen()
Screen.onkey(move_forward, "w")
Screen.onkey(move_backward, "s")
Screen.onkey(move_left, "a")
Screen.onkey(move_right, "d")

Screen.exitonclick()