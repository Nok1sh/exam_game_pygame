import pygame
from structures_and_parameters.parameters_game import WindowParams


class Trader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size: int = 1
        self.image = pygame.image.load("textures/store/steampunk_trader.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size, self.image.get_height() // self.size))
        self.rect = self.image.get_rect()
        self.rect.center = ((WindowParams.WIDTH//4)*3-50, WindowParams.HEIGHT//2+100)


class StoreMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("textures/store/store_menu.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 1.5, self.image.get_height() // 1))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2)