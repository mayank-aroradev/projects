import turtle
import os
import pandas

# Create the screen
screen = turtle.Screen()
screen.title("US STATES GAME")

# Load the image
image = os.path.join(os.path.dirname(__file__), "blank_states_img.gif")
screen.addshape(image)
turtle.shape(image)

# Load the CSV data properly
data_path = os.path.join(os.path.dirname(__file__), "50_states.csv")
data = pandas.read_csv(data_path)
guessed_states = []
while len(guessed_states) < 50:
    all_states = data.state.to_list()

    # Ask user for a state name
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    print(answer_state)

    # If correct, write state name on map
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

screen.exitonclick()

