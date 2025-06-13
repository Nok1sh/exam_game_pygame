import pygame
from structures_and_parameters.parameters_game import Textures, ActionParams
from structures_and_parameters.parameters_game import WindowParams


class RangeBossEnemyRender(pygame.sprite.Sprite):
    def __init__(self, enemy):
        super().__init__()
        self.boss_range_enemy = enemy
        self.width: int = 70
        self.height: int = 70
        self.size_boss_range_enemy: int = 10
        self.image = pygame.image.load(f"textures/boss_range_enemy/boss_range_enemy1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (
        self.image.get_width() // self.size_boss_range_enemy, self.image.get_height() // self.size_boss_range_enemy))
        self.rect = self.image.get_rect()
        self.rect.center = self.boss_range_enemy.rect.center
        self.number_image: int = 1
        self.animation_range_enemy: int = 0
        self.speed_rotation: int = 10

    def swap_image(self):
        self.image = Textures.BOSS_RANGE_ENEMY[self.number_image - 1]
        self.image = pygame.transform.scale(self.image, (
        self.image.get_width() // self.size_boss_range_enemy, self.image.get_height() // self.size_boss_range_enemy))

    def update(self):
        WindowParams.SCREEN.blit(self.image, self.rect)
        self.rect.center = self.boss_range_enemy.rect.center
        self.animation_range_enemy += ActionParams.TIME_ANIMATION_MELEE_ENEMY
        if self.animation_range_enemy >= 1 / self.speed_rotation:
            self.animation_range_enemy -= 1.0 / self.speed_rotation
            self.swap_image()
            self.number_image = self.number_image % 24 + 1