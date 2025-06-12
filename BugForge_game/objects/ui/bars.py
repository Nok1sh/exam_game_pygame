import pygame
from structures_and_parameters.parameters_game import WindowParams, ActionParams, Textures
import math


class ManaBar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.size_width: int = 2
        self.size_height: int = 3
        self.image = pygame.image.load("textures/manabar/manabar_5.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_width, self.image.get_height()//self.size_height))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = WindowParams.HEIGHT-45

    def __recovery_mana_bar(self) -> None:
        if self.player.mana_pool != 5:
            if pygame.time.get_ticks() - ActionParams.LAST_MANA_RECOVERED >= ActionParams.RECOVERY_MANA_BAR:
                self.player.mana_pool += 1
                ActionParams.LAST_MANA_RECOVERED = pygame.time.get_ticks()

    def update(self) -> None:
        mana_bar_textures: list = Textures.MANA_BARS
        self.image = mana_bar_textures[self.player.mana_pool]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.__recovery_mana_bar()


class HealthBar(pygame.sprite.Sprite):

    FLAG_SWAP: bool = False

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.size_width: int = 2
        self.size_height: int = 3
        self.image = pygame.image.load("textures/healthbar2/healthbar_4.png").convert_alpha() \
            if ActionParams.FLAG_UPPER_HEALTH_BAR \
            else pygame.image.load("textures/healthbar/healthbar_3.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect()
        self.rect.y = WindowParams.HEIGHT - 45
        self.rect.right = WindowParams.WIDTH - (8 if ActionParams.FLAG_UPPER_HEALTH_BAR else -52)

    def update(self) -> None:
        if HealthBar.FLAG_SWAP:
            HealthBar.FLAG_SWAP = False
            self.rect.y = WindowParams.HEIGHT - 45
            self.rect.right = WindowParams.WIDTH - (8 if ActionParams.FLAG_UPPER_HEALTH_BAR else -52)
        health_bar_textures: list = Textures.HEALTH_BARS_BIG if ActionParams.FLAG_UPPER_HEALTH_BAR \
            else Textures.HEALTH_BARS
        self.image = health_bar_textures[math.ceil(self.player.health_bar)]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))


class MoneyBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_width: int = 1
        self.size_height: int = 2
        self.image = pygame.image.load("textures/money_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect()
        self.rect.center = (135, 22)