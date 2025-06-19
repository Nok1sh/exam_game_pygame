import pygame
from structures_and_parameters.parameters_game import WindowParams, Textures
Textures.load_all()


class Doors(pygame.sprite.Sprite):
    def __init__(self, line: str, x=None, y=None):
        super().__init__()
        self.size_door: int = 2
        self.image = Textures.DOORS[line]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_door, self.image.get_height() // self.size_door))
        if line == 'vertical':
            self.rect = self.image.get_rect()
            self.rect.center = (x, WindowParams.HEIGHT//2)
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (WindowParams.WIDTH//2, y)
