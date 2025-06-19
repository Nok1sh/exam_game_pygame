import pygame
from structures_and_parameters.parameters_game import Textures
Textures.load_all()


class Walls(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        tile_width, tile_height = Textures.WALL.get_size()
        for tx in range(0, width, tile_width):
            for ty in range(0, height, tile_height):
                self.image.blit(Textures.WALL, (tx, ty))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
