import pygame
import math
from objects.action_objects.enemies_direction.enemies_model import Enemy
from .melee_enemy_render import MeleeEnemyRender


class MeleeEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self, x, y)
        self.width_collision: int = 79
        self.height_collision: int = 79
        self.rect = pygame.Rect(
            x,
            y,
            self.width_collision,
            self.height_collision
        )
        self.speed: int = 4
        self.push_distance: int = 2
        self.attack_damage: float = 0.5
        self.attack_range: int = 90
        self.render_enemy = MeleeEnemyRender(self)

    def move_towards_enemy(self, player, walls) -> None:
        distance_x: int = player.rect.x - self.rect.x
        distance_y: int = player.rect.y - self.rect.y
        distance: float = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if distance > 0:
            distance_x /= distance
            distance_y /= distance

        if self.rect.colliderect(player.rect):
            self.rect.x -= distance_x * self.push_distance
            self.rect.y -= distance_y * self.push_distance
        else:
            new_x: float = self.rect.x + distance_x * self.speed
            new_y: float = self.rect.y + distance_y * self.speed

            if self.can_move(new_x, new_y, walls):
                self.rect.x = int(new_x)
                self.rect.y = int(new_y)

    def check_attack(self, player, projectiles) -> None:
        distance_x: int = player.rect.x - self.rect.x
        distance_y: int = player.rect.y - self.rect.y
        distance: float = math.sqrt(distance_x ** 2 + distance_y ** 2)
        if distance <= self.attack_range and self.current_attack_cooldown <= 0:
            self.attack(player, distance_x, distance_y, projectiles)

    def attack(self, player, distance_x: float, distance_y: float, projectiles) -> None:
        if self.current_attack_cooldown <= 0:
            player.take_damage(self.attack_damage)
            self.rect.x -= distance_x * self.push_distance
            self.rect.y -= distance_y * self.push_distance
            self.current_attack_cooldown = self.attack_cooldown

