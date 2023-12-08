from collections import namedtuple

# Define some tuples to make things easier
Point = namedtuple("Point", ('x', 'y'))
Size = namedtuple("Size", ("width", "height"))
Color = namedtuple("Color", ('r', 'g', 'b'))

# Define the window size
WINDOW_SIZE = Size(1024, 576)

FONT_SIZE = WINDOW_SIZE.height // 10

# Make the body part size a fraction of the window size so that can change without reaking havoc
BODY_PART_SIZE = Size(25, 25)

# The grid size is useful for calculating where the apple should go and if the snake has gone off-screen
GRID_SIZE = Size(WINDOW_SIZE.width // BODY_PART_SIZE.width, WINDOW_SIZE.height // BODY_PART_SIZE.height)

# The snake color is a nice blue
SNAKE_COLOR = Color(33, 88, 238)

# The background color is white
BACKGROUND_COLOR = Color(255, 255, 255)

# The text color is black
TEXT_COLOR = Color(0, 0, 0)

# The apple color is red                                                (duh)
APPLE_COLOR = Color(255, 0, 0)

# The snake speed is how much it will jump each frame, so this needs to be the same size of each body part
SNAKE_SPEED = BODY_PART_SIZE.width

FRAME_RATE = 60

# How mich time should be in between each update
# The more this is the slower the snake is and the less this is the faster the snake is
UPDATE_INTERVAL = 100