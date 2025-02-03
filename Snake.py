
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
onkey(lambda: direction(10, 0), 'Right')
onkey(lambda: direction(-10, 0), 'Left')
onkey(lambda: direction(0, 10), 'Up')
onkey(lambda: direction(0, -10), 'Down')
move()
done()
