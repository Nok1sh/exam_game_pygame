import pygame
from structures_and_parameters.parameters_game import Textures
Textures.load_all()


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.size_barrel: int = 5
        self.image = pygame.image.load("textures/barrel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_barrel, self.image.get_height() // self.size_barrel))
        self.rect = self.image.get_rect()
        self.x: int = x
        self.y: int = y
        self.rect.center = (self.x, self.y)
        self.health: int = 2
