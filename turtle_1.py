from turtle import Turtle , Screen
import random
is_race_on = False


Screen = Screen() 
Screen.setup(width=500, height=400)
user_input = Screen.textinput(title="make your own bet ", prompt="which turtle will win the race? Enter a colour")
colors = ["red","orange","yellow","green","blue","purple"]
Y_positions = [-70,-40,-10,20,50,80]
all_turtle = []


for turtle_index in range(0,6):

    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])

    tim.penup()
    tim.goto(x=-230,y=Y_positions[turtle_index])
    all_turtle.append(tim)

if user_input:
    is_race_on = True

while is_race_on:


    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f"ypu've won! the {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner ")


        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


Screen.exitonclick()