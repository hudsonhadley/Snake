import pygame
from settings import WINDOW_SIZE, Point, SNAKE_SPEED, BODY_PART_SIZE, GRID_SIZE
from body_part import BodyPart
from apple import Apple

class Snake(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

        self.body = [BodyPart(0, 0)]
        self.add(self.body[0])
        self.velocity = pygame.Vector2(0, 0)

        self.body[0].rect.x = BODY_PART_SIZE.width * (GRID_SIZE.width // 2)
        self.body[0].rect.y = BODY_PART_SIZE.height * (GRID_SIZE.height // 2)

        self.previous_body_rect = []
        self.updated = False



    def down(self):
        """
        Sets the velocity to go down if the direction is not currently going up
        """
        if self.velocity != pygame.Vector2(0, -SNAKE_SPEED) and self.updated:
            self.velocity = pygame.Vector2(0, SNAKE_SPEED)

            self.updated = False


    def up(self):
        """
        Sets the velocity to go up if the direction is not currently going down
        It will also not change if the screen has not been updated yet to prevent stuff turning into itself really quickly
        """
        if self.velocity != pygame.Vector2(0, SNAKE_SPEED) and self.updated:
            self.velocity = pygame.Vector2(0, -SNAKE_SPEED)

            self.updated = False

    def left(self):
        """
        Sets the velocity to go left if the direction is not currently going right
        It will also not change if the screen has not been updated yet to prevent stuff turning into itself really quickly
        """
        if self.velocity != pygame.Vector2(SNAKE_SPEED, 0) and self.updated:
            self.velocity = pygame.Vector2(-SNAKE_SPEED, 0)

            self.updated = False

    def right(self):
        """
        Sets the velocity to go right if the direction is not currently going left.
        It will also not change if the screen has not been updated yet to prevent stuff turning into itself really quickly
        """
        if self.velocity != pygame.Vector2(-SNAKE_SPEED, 0) and self.updated:
            self.velocity = pygame.Vector2(SNAKE_SPEED, 0)

            self.updated = False

    def update(self):
        """
        Updates the snake by moving the head and updating all the other body parts.
        """

        self.previous_body_rect = [Point(i.rect.x, i.rect.y) for i in self.body]
        self.body[0].rect.x += self.velocity.x
        self.body[0].rect.y += self.velocity.y

        for i in range(1, len(self.body)):

            self.body[i].rect.x = self.previous_body_rect[i - 1].x
            self.body[i].rect.y = self.previous_body_rect[i - 1].y

        self.updated = True


    def is_dead(self):
        """
        Sees if the snake is dead
        :return: False if it is not dead, True if it is dead
        """
        head_rect = self.body[0].rect

        # If we go off the screen...
        # To the left
        if head_rect.left < 0:
            return True
        # To the top
        if head_rect.top < 0:
            return True
        # To the right
        if head_rect.right > WINDOW_SIZE.width:
            return True
        # To the bottom
        if head_rect.bottom > WINDOW_SIZE.height:
            return True

        # Go through the whole snake besides the head and see if the head's coordinates intersect with any others
        # Note: the head can only hit the 2nd body part if the user goes in the opposite direction
        for i in range(2, len(self.body)):
            if head_rect == self.body[i]:
                return True

        return False


    def add_new_body_part(self):
        """
        Adds a new body part at the end of the snake
        """
        previous_last_body_part = self.previous_body_rect[len(self.previous_body_rect) - 1]

        new_body_part = BodyPart(previous_last_body_part.x, previous_last_body_part.y)
        self.body.append(new_body_part)
        self.add(new_body_part)



    def length(self):
        return len(self.body)