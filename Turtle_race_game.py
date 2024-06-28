from turtle import Turtle, Screen
import random

screen = Screen()

is_race_on = False
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='What colour turtle will win the race?: ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtle = []


for turtle_index in range(0,6):
    tim = Turtle(shape='turtle')
    tim.penup()
    tim.goto(x=-230, y=-100+(turtle_index*40))
    tim.color(colors[turtle_index])
    all_turtle.append(tim)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            wining_color = turtle.pencolor()
            if wining_color == user_bet:
                print("You have won !")
            else:
                print(f"You have lost, the winning color is {wining_color}")
        turtle.forward(random.randint(0,10))

screen.exitonclick()


