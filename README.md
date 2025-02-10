# Python Snake.py 
Just a for fun python project of the snake game recreated in python on a spare Afternoon, this wasn't a class assignment, i was just bored and wanted to mess around with some code and test out coding in the visual studios code ide with it. 

This program runs within a python IDE like the before mentioned Visual Studio Code or Pycharm/ or any python ide of choice using a Python graphical gui that appears on run. You will need to use pip to install a freegames libary to make the graphics work.

To run:
1. Open snake.py in your python ide of choice
2. In terminal, run `pip install freegames` to install a required dependency for the graphics that renders the squares, it's admitedly a bit basic but this was a weekend whim done in a hour or two. 
3. The game should run inside a graphical gui from the Turtle Library.

Controls: Press the arrow keys (or WASD) to move the snake around the screen. 
The snake will grow as it eats the red food blocks. 
If the snake runs into the wall or itself, a gameover will happen and then the game will restart.

![Example](https://github.com/user-attachments/assets/bccee309-464f-4199-87b8-50978d6a3f90)

Some additional code was also added to support and implement a respawn from death, as the game initially ended with a blank screen on death and was originally never continuable/playable again after the first death. 

I also quickly added some basic implementation for WASD and wasd controls, which didn't take much, then refactored the code to implement the respawn/continue function by coding a restart function and reimplementing it into the gameplay loop so on death, instead of crashing and pausing, the structured code would loop properly like a fresh start. 


