
# # Python-Snake
# Just a for fun python project of a basic implementation of Snake in python 

# This program runs within a python IDE like visual studios or Pycharm using a graphical gui that appears when you press run in a code complier to run the program.

# To run:
# 1. Open snake.py in your python ide of choice
# 2. In terminal, run `pip install freegames` to install a required dependency
# 3. The game should run inside a graphical gui from the Turtle Library.

# Controls: Press the arrow keys (or WASD) to move the snake around the screen. 
# The snake will grow as it eats the red food blocks. 
# If the snake runs into the wall or itself, the game will restart.

from turtle import *
from random import randrange

# If this import fails, run `pip install freegames` in terminal
from freegames import square, vector
from time import sleep

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# Controls the direction of the snake
def direction(x, y):
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# When the snake dies, this new function will restart the game after xs. 
def restart():
    global snake, food, aim
    snake = [vector(10, 0)]
    food = vector(0, 0)
    aim = vector(0, -10)
    
    sleep(2)
    clear()
    
    move()


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()

        # Added Restart function, when you die, it waits x seconds to restart the game

        restart()
        return

    snake.append(head)

    if head == food:
        food.x = randrange(-12, 12) * 10
        food.y = randrange(-12, 12) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'green')

    square(food.x, food.y, 9, 'red')
    update()
    ontimer(move, 50)


setup(420, 420, 370, 0)
hideturtle()
tracer(False) # Draws the blocks bit by bit on True, slows down the game dramatically

listen()

# Arrow key controls 
onkey(lambda: direction(10, 0), 'Right')
onkey(lambda: direction(-10, 0), 'Left')
onkey(lambda: direction(0, 10), 'Up')
onkey(lambda: direction(0, -10), 'Down')

#  W
# ASD key controls 
    # (lowercase)
onkey(lambda: direction(10, 0), 'd')
onkey(lambda: direction(-10, 0), 'a')
onkey(lambda: direction(0, 10), 'w')
onkey(lambda: direction(0, -10), 's')
    #(UPPERCASE)
onkey(lambda: direction(10, 0), 'D')
onkey(lambda: direction(-10, 0), 'A')
onkey(lambda: direction(0, 10), 'W')
onkey(lambda: direction(0, -10), 'S')

move()
done()
