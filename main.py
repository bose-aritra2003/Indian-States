# Indian States Game

# User will keep on writing name of states and if name is correct
# then the names be one by one pointed on the Indian map.
# Game concept from ---> https://www.sporcle.com/games/g/states

from turtle import Turtle, Screen
import pandas

IMAGE_FILE = "blank_states_img.gif"
STATES_FILE = "28_states.csv"
STATE_COUNT = 28

my_screen = Screen()
my_screen.setup(width=500, height=678)
my_screen.title("Indian States Game")
my_screen.addshape(IMAGE_FILE)  # For the background

my_turtle = Turtle()
my_turtle.shape(IMAGE_FILE)

my_screen.tracer(False)

data = pandas.read_csv(STATES_FILE)
all_states = data.state.tolist()
guessed_states = []

while len(guessed_states) <= STATE_COUNT:
    guess = (my_screen.textinput(title=f"{len(guessed_states)}/28 States guessed correctly",
                                 prompt="Guess another state\'s name")).title()
    # If user has finished guessing
    if guess == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_states_data = pandas.DataFrame(missed_states).to_csv("states_to_learn.csv")
        break

    # If correct guess
    elif guess in all_states:
        guessed_states.append(guess)
        stateTurtle = Turtle()
        stateTurtle.hideturtle()
        stateTurtle.penup()
        x_pos = int(data[data.state == guess].x)
        y_pos = int(data[data.state == guess].y)
        stateTurtle.goto(x_pos, y_pos)
        stateTurtle.write(f"{guess}", font=('Arial', 8, 'bold'))
        all_states.remove(guess)
        my_screen.update()
