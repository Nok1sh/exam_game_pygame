import pygame
from structures_and_parameters.parameters_game import Textures, ActionParams
from structures_and_parameters.parameters_game import WindowParams


class MeleeEnemyRender(pygame.sprite.Sprite):
    def __init__(self, melee_enemy):
        super().__init__()
        self.size_melee_enemy: int = 10
        self.image = pygame.image.load(f"textures/melee_enemy/melee_enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (
        self.image.get_width() // self.size_melee_enemy, self.image.get_height() // self.size_melee_enemy))
        self.rect = self.image.get_rect()
        self.melee_enemy = melee_enemy
        self.rect.center = self.melee_enemy.rect.center
        self.number_image: int = 1
        self.animation_melee_enemy: int = 0
        self.speed_rotation: int = 40

    def swap_image(self):
        self.image = Textures.MELEE_ENEMY[self.number_image - 1]
        self.image = pygame.transform.scale(self.image, (
            self.image.get_width() // self.size_melee_enemy, self.image.get_height() // self.size_melee_enemy))

    def update(self):
        WindowParams.SCREEN.blit(self.image, self.rect)
        self.rect.center = self.melee_enemy.rect.center
        self.animation_melee_enemy += ActionParams.TIME_ANIMATION_MELEE_ENEMY
        if self.animation_melee_enemy >= 1 / self.speed_rotation:
            self.animation_melee_enemy -= 1.0 / self.speed_rotation
            self.swap_image()
            self.number_image = self.number_image % 5 + 1
