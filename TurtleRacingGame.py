# Project 5-Turtle Racing Game
# the project is going to be simple racing game with a simple GUI
# here the user is going to input the no. of racers participating in the game
# and then the race is automatically started showing it in a screen and then the
# winner is going to be declared
import turtle
# import time
import random

WIDTH = 500
HEIGHT = 500
COLORS = ["red", "yellow", "orange", "blue", "green", "purple", "black", "cyan", "brown", 'pink']


def assort_colors_turtles(turtles):
    #     here we alot random colors to the racers and create the turtles and return them in the form of a list
    random.shuffle(COLORS)
    colors = COLORS[:turtles]
    return colors


def create_turtles(colors):
    # the below list will contain all the turtles which will be assigned
    # with their respective colors and starting positions
    turtles = []
    space_x = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        # this function will set the position of the turtle at the starting line setpos(x_coordinate,y_coordinate)
        racer.setpos(-(WIDTH // 2) + (i + 1) * space_x, -(HEIGHT // 2) + 15)
        racer.pendown()
        turtles.append(racer)
    return turtles


def race(colors):
    # the below function will take the no of racers from the user as input
    turtles = create_turtles(colors)
    #     now this function will start the race
    while True:
        for turtle in turtles:
            move = random.randrange(1, 20)
            turtle.forward(move)

            x, y = turtle.pos()
            if y >= WIDTH // 2 - 15:
                return colors[turtles.index(turtle)]


def get_no_of_racers():
    while True:
        players = input("enter the no. of racers (2-10): ")
        if players.isdigit():
            players = int(players)
        else:
            print("Invalid input!!..")
            continue
        if 2 <= players <= 10:
            return players
        else:
            print("please enter a number between (2-10)! ")


def __fun__turtle():
    # 2d gui
    # the below function explicitly calls the turtle screen
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!!")


# print(racers)


racers = get_no_of_racers()
print(racers)
__fun__turtle()
colors = assort_colors_turtles(racers)
# create_turtles(colors)
winner = race(colors)
print("The winner is "+winner+" turtle !!!")
turtle.done()


