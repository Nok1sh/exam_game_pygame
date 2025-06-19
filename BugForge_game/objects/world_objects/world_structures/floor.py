import pygame
from structures_and_parameters.parameters_game import Textures
Textures.load_all()


class Floor:
    surface = None

    @staticmethod
    def init(screen_width, screen_height):
        tile = Textures.FLOOR
        Floor.surface = pygame.Surface((screen_width, screen_height))
        for tx in range(0, screen_width, tile.get_width()):
            for ty in range(0, screen_height, tile.get_height()):
                Floor.surface.blit(tile, (tx, ty))

    @staticmethod
    def draw(screen):
        screen.blit(Floor.surface, (0, 0))
