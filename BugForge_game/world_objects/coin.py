import pygame
from structures_and_parameters.parameters_game import ActionParams, Textures


class Coin(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.size: int = 3
        self.score: int = 50
        self.image = pygame.image.load("textures/coin/money_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size, self.image.get_height()//self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_rotation: int = 7
        self.animation_money: int = 0
        self.number_image: int = 1

    def update(self) -> None:
        self.animation_money += ActionParams.TIME_ANIMATION_COIN
        if self.animation_money >= 1.0 / self.speed_rotation:
            self.number_image = self.number_image % 6 + 1
            self.animation_money -= 1.0 / self.speed_rotation
        self.image = Textures.COIN[self.number_image-1]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size, self.image.get_height() // self.size))
