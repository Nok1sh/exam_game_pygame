import pygame
import math
import random
from ...world_objects.potion import Potion
from ...world_objects.coin import Coin
from structures_and_parameters.parameters_game import WindowParams, Textures, ActionParams


class MagicBall(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, distance_x=None, distance_y=None, line_move=None):
        super().__init__()
        self.line_move = line_move
        self.attack_damage: float = 1
        self.speed_move: int = 7
        self.size_width: int = 8
        self.size_height: int = 8
        self.textures_big = Textures.MAGIC_BALL_BIG if self.line_move else Textures.MAGIC_BALL_BIG_ENEMY
        self.textures_small = Textures.MAGIC_BALL_SMALL if self.line_move else Textures.MAGIC_BALL_SMALL_ENEMY
        self.image = self.textures_big
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect(center=(x, y))
        if not self.line_move:
            self.line_attack = math.sqrt(distance_x**2 + distance_y**2) if math.sqrt(distance_x**2 + distance_y**2) != 0 else 1
            self.velocity_x: float = self.speed_move * (distance_x/self.line_attack)
            self.velocity_y: float = self.speed_move * (distance_y/self.line_attack)
        else:
            self.speed_x: int = 0
            self.speed_y: int = 0
        self.animation_move: float = 0
        self.speed_rotation: int = 5
        self.swap_image: bool = False
        self.current_image: str = 'big'  # small

    def __update_objects(self, walls, current_enemies=None, barrels=None, columns=None, player=None, coins=None, potions=None):
        if player and self.rect.colliderect(player.rect):
            player.take_damage(self.attack_damage)
            self.kill()

        elif not (0 < self.rect.center[0] < WindowParams.WIDTH) or not (0 < self.rect.center[1] < WindowParams.HEIGHT):
            self.kill()
        elif pygame.sprite.spritecollide(self, walls, False) or \
                (player and not current_enemies) or \
                (columns and pygame.sprite.spritecollide(self, columns, False)):
            self.kill()
        elif barrels:
            collided_barrels = pygame.sprite.spritecollide(self, barrels, False)
            for barrel in collided_barrels:
                barrel.health -= 1
                if barrel.health <= 0:
                    barrel.kill()
                    chance_drop: float = random.random()
                    if chance_drop <= 0.2:
                        coins.add(Coin(barrel.x, barrel.y))
                    elif chance_drop <= 0.4:
                        potions.add(Potion(barrel.x, barrel.y, "health"))
                    elif chance_drop <= 0.7:
                        potions.add(Potion(barrel.x, barrel.y, "mana"))
                self.kill()

    def update(self, walls, current_enemies=None, barrels=None, columns=None, player=None, coins=None, potions=None) -> None:
        self.rect.x += self.velocity_x if not self.line_move else self.speed_x
        self.rect.y += self.velocity_y if not self.line_move else self.speed_y
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
        self.__update_objects(walls, current_enemies, barrels, columns, player, coins, potions)


class MagicBallPlayer(MagicBall, pygame.sprite.Sprite):
    """
    Hero's shells
    """
    def __init__(self, center: tuple, line_move: str):
        pygame.sprite.Sprite.__init__(self)
        MagicBall.__init__(self, center[0], center[1], line_move=line_move)
        self.diagonal_move_rate: float = 0.7071
        self.line_move = line_move
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


class MagicBallEnemy(MagicBall, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, distance_x: float, distance_y: float):
        pygame.sprite.Sprite.__init__(self)
        MagicBall.__init__(self, x, y, distance_x, distance_y)


