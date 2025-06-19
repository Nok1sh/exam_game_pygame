import pygame
from structures_and_parameters.parameters_game import Textures
Textures.load_all()


class Column(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, random_image):
        super().__init__()
        self.size_column: int = 5
        self.x: int = x
        self.y: int = y
        self.random_image = random_image
        self.image = pygame.image.load(f"textures/columns/column_{self.random_image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_column, self.image.get_height() // self.size_column))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
