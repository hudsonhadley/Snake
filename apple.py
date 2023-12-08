import pygame.sprite

from settings import BODY_PART_SIZE, APPLE_COLOR, WINDOW_SIZE, GRID_SIZE

from random import randint


class Apple(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.Surface(BODY_PART_SIZE)
        self.image.fill(APPLE_COLOR)
        self.rect = self.image.get_rect()


    def place(self):
        self.rect.x = randint(0, GRID_SIZE.width - 1) * BODY_PART_SIZE.width
        self.rect.y = randint(0, GRID_SIZE.height - 1) * BODY_PART_SIZE.height