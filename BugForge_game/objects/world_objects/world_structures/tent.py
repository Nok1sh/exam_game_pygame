import pygame
from structures_and_parameters.parameters_game import WindowParams, Textures
Textures.load_all()


class Tent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_tent: int = 5
        self.image = pygame.image.load("textures/store/tent.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_tent, self.image.get_height() // self.size_tent))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH//2, WindowParams.HEIGHT//2)
