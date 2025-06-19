import pygame
from structures_and_parameters.parameters_game import Textures
Textures.load_all()


class BackgroundOptions:
    surface = None

    @staticmethod
    def init(screen_width, screen_height):
        tile = pygame.image.load(f"textures/background_options.png").convert()
        BackgroundOptions.surface = pygame.Surface((screen_width, screen_height))
        for tx in range(0, screen_width, tile.get_width()):
            for ty in range(0, screen_height, tile.get_height()):
                BackgroundOptions.surface.blit(tile, (tx, ty))

    @staticmethod
    def draw(screen):
        screen.blit(BackgroundOptions.surface, (0, 0))
