import pygame
import random
import math
from objects.action_objects.projectiles_direction.magic_balls import MagicBallEnemy
from objects.action_objects.enemies_direction.enemies_model import Enemy
from .range_enemy_render import RangeEnemyRender


class RangeEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self, x, y)
        self.distance_attack: int = 350
        self.evade_chance: float = 0.3
        self.attack_cooldown: float = 125
        self.width_collision: int = 77
        self.height_collision: int = 77
        self.rect = pygame.Rect(
            x,
            y,
            self.width_collision,
            self.height_collision
        )
        self.render_enemy = RangeEnemyRender(self)

    def move_towards_enemy(self, player, walls) -> None:
        distance_x: int = player.rect.x - self.rect.x
        distance_y: int = player.rect.y - self.rect.y
        distance: float = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if distance > 0:
            distance_x /= distance
            distance_y /= distance

        new_x: float = 0
        new_y: float = 0
        if distance < self.distance_attack - 30:
            if random.random() < self.evade_chance:
                side_evade: int = random.choice([-1, 1])
                new_x = -distance_x * side_evade * self.speed
                new_y = -distance_y * side_evade * self.speed
            else:
                new_x = -distance_x * self.speed
                new_y = -distance_y * self.speed
        elif distance > self.distance_attack + 30:
            new_x = distance_x * self.speed
            new_y = distance_y * self.speed

        new_x += self.rect.x
        new_y += self.rect.y
        if self.can_move(new_x, new_y, walls):
            self.rect.x = int(new_x)
            self.rect.y = int(new_y)

    def check_attack(self, player, projectiles) -> None:
        distance_x: int = player.rect.x - self.rect.x
        distance_y: int = player.rect.y - self.rect.y
        distance: float = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if distance <= self.distance_attack and self.current_attack_cooldown <= 0:
            self.attack(player, distance_x, distance_y, projectiles)

    def attack(self, player, distance_x: float, distance_y: float, projectiles) -> None:
        if self.current_attack_cooldown <= 0:
            projectile = MagicBallEnemy(self.rect.centerx, self.rect.centery, distance_x, distance_y)
            projectiles.add(projectile)
            self.current_attack_cooldown = self.attack_cooldown