This is a simplified version of the snake game.
A 'snake' starts out about the middle of the screen 1 long.
An apple is randomly placed on the screen. Once the player hits an arrow key or WASD,
the snake begins to move in that direction. If they collect the apple, they grow by 1
and the apple is replaced somewhere on the screen. This continues until the snake runs
into itself or hits a wall. The files in this repository are as follows:

[apple.py]() - Holds the Apple class used
to construct an apple and define its position.

[body_part.py]() - Holds the BodyPart
class that is used to construct the snake.

[high_score.py]() - Holds the current
high score (this can be reset whenever by making
high_score = 0).

[main.py]() - Where the game actually happens. 
Variables are either drawn from settings,
apple, body_part, snake, high_score, or initialized
at the beginning. It then goes into the game loop,
which continually checks for input at whatever the
frame rate is set at, but updates the screen at a
slower rate to ensure the snake is jumpy and
discrete to the player. Once a player dies (i.e. 
the snake hits itself or goes off-screen), the loop
ends and checks if the player wants to restart while
displaying the high score and score. If they do
want to restart, it goes right back into the loop.

[settings.py]() - Where constant variables we don't
ever change are defined. These include frame rate,
update rate, colors, window size, and body part size.
These values can be changed if desired, but with
caution. Some like colors are harmless. But others
like update rate can be dangerous if too slow and
frustrating for any player attempting to make quick
moves.

[snake.py]() - Holds the Snake class that is used to 
define the snake. Snake is a simple class whose main
part is just a list of body parts. It's main methods
are the add new body part, directional functions
changing the velocity of the snake, and is dead. 
All of these functions are vitally important to the
game and where most of the problem-solving for this
project occurred.
