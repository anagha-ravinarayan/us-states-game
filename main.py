import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image_file_name = "blank_states_img.gif"
screen.addshape(name=image_file_name)
turtle.shape(image_file_name)

artist = turtle.Turtle()
artist.hideturtle()
artist.penup()

states_file = pandas.read_csv("50_states.csv")
states = states_file.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess = turtle.textinput(title=f"{len(guessed_states)}/50 states are right", prompt="Guess the state").title()
    if guess == "Exit":
        break
    if guess in states:
        guessed_states.append(guess)
        states_file_row = states_file[states_file.state == guess]
        artist.setpos(x=int(states_file_row.x), y=int(states_file_row.y))
        artist.write(guess)
