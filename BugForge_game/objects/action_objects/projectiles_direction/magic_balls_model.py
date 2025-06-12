import pygame
import math
from typing import Dict
from structures_and_parameters.parameters_game import WindowParams, Textures, ActionParams


class MagicBall(pygame.sprite.Sprite):
    """
    Hero's shells
    """
    def __init__(self, center: tuple, line_move: str):
        super().__init__()
        self.speed_x: int = 0
        self.speed_y: int = 0
        self.speed_move: int = 7
        self.diagonal_move_rate: float = 0.7071
        self.size_width: int = 8
        self.size_height: int = 8
        self.line_move = line_move
        self.textures_big = Textures.MAGIC_BALL_BIG
        self.textures_small = Textures.MAGIC_BALL_SMALL
        self.image = self.textures_big
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_width, self.image.get_height()//self.size_height))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.animation_move: float = 0
        self.speed_rotation: int = 5
        self.swap_image: bool = False
        self.current_image: str = 'big'  # small
        self.__change_speed_ball(line_move)

    def __change_speed_ball(self, line_move) -> None:
        if line_move == 'right':
            self.speed_x = self.speed_move
        elif line_move == 'left':
            self.speed_x = -self.speed_move
        elif line_move == 'top':
            self.speed_y = -self.speed_move
        elif line_move == 'bottom':
            self.speed_y = self.speed_move
        elif line_move == 'right_top':
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
        elif line_move == 'right_bottom':
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
        elif line_move == 'left_top':
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
        elif line_move == 'left_bottom':
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate

    def __update_walls(self, walls) -> None:
        if not (0 < self.rect.center[0] < WindowParams.WIDTH) or not(0 < self.rect.center[1] < WindowParams.HEIGHT):
            self.kill()
        walls_collision = pygame.sprite.spritecollide(self, walls, False)
        if walls_collision:
            self.kill()

    def update(self, walls) -> None:
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        self.animation_move += ActionParams.TIME_ANIMATION_MAGIC_BALL
        if self.animation_move >= 1 / self.speed_rotation:
            self.animation_move -= 1.0 / self.speed_rotation
            self.swap_image = True
        if self.swap_image:
            if self.current_image == 'big':
                self.image = self.textures_small
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
                self.current_image = 'small'
            else:
                self.image = self.textures_big
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
                self.current_image = 'big'
        self.swap_image = False
        self.__update_walls(walls)


class Projectile(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, distance_x: float, distance_y: float):
        super().__init__()
        self.attack_damage: float = 1
        self.projectile_speed: float = 7
        self.size_width: int = 8
        self.size_height: int = 8
        self.textures_big = Textures.MAGIC_BALL_BIG_ENEMY
        self.textures_small = Textures.MAGIC_BALL_SMALL_ENEMY
        self.image = self.textures_big
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect(center=(x, y))
        self.line_attack = math.sqrt(distance_x**2 + distance_y**2) if math.sqrt(distance_x**2 + distance_y**2) != 0 else 1
        self.velocity_x: float = self.projectile_speed * (distance_x/self.line_attack)
        self.velocity_y: float = self.projectile_speed * (distance_y/self.line_attack)
        self.animation_move: float = 0
        self.speed_rotation: int = 5
        self.swap_image: bool = False
        self.current_image: str = 'big'  # small

    def update(self, current_enemies, player, walls, barrels=None, columns=None) -> None:
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        self.animation_move += ActionParams.TIME_ANIMATION_MAGIC_BALL
        if self.animation_move >= 1 / self.speed_rotation:
            self.animation_move -= 1.0 / self.speed_rotation
            self.swap_image = True
        if self.swap_image:
            if self.current_image == 'big':
                self.image = self.textures_small
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // self.size_width,
                                                     self.image.get_height() // self.size_height))
                self.current_image = 'small'
            else:
                self.image = self.textures_big
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // self.size_width,
                                                     self.image.get_height() // self.size_height))
                self.current_image = 'big'
        self.swap_image = False
        if self.rect.colliderect(player.rect):
            player.take_damage(self.attack_damage)
            self.kill()

        elif not (0 < self.rect.center[0] < WindowParams.WIDTH) or not (0 < self.rect.center[1] < WindowParams.HEIGHT):
            self.kill()
        elif pygame.sprite.spritecollide(self, walls, False) or \
                pygame.sprite.spritecollide(self, columns, False) or not current_enemies:
            self.kill()