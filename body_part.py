import pygame

from settings import BODY_PART_SIZE, SNAKE_COLOR

class BodyPart(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface(BODY_PART_SIZE)
        self.image.fill(SNAKE_COLOR)
        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y