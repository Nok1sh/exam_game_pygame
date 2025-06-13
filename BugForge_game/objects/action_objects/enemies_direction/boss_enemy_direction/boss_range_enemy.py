import pygame
import math
from objects.action_objects.projectiles_direction.magic_balls import MagicBallEnemy
from objects.action_objects.enemies_direction.range_enemy_direction.range_enemy import RangeEnemy
from .boss_range_enemy_render import RangeBossEnemyRender


class RangeBossEnemy(RangeEnemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        RangeEnemy.__init__(self, x, y)
        self.width_collision: int = 85
        self.height_collision: int = 85
        self.rect = pygame.Rect(
            x,
            y,
            self.width_collision,
            self.height_collision
        )
        self.speed: int = 2
        self.ultra_attack_cooldown: int = 175
        self.distance_attack: int = 500
        self.max_health: float = 25
        self.current_health: float = self.max_health
        self.render_enemy = RangeBossEnemyRender(self)

    def move_towards_enemy(self, player, walls) -> None:
        distance_x: int = player.rect.x - self.rect.x
        distance_y: int = player.rect.y - self.rect.y
        distance: float = math.sqrt(distance_x**2 + distance_y**2)

        if distance > 0:
            distance_x /= distance
            distance_y /= distance

        if self.rect.colliderect(player.rect):
            pass
        else:
            new_x: float = self.rect.x + distance_x*self.speed
            new_y: float = self.rect.y + distance_y * self.speed

            if self.can_move(new_x, new_y, walls):
                self.rect.x = int(new_x)
                self.rect.y = int(new_y)

    def attack(self, player, distance_x: float, distance_y: float, projectiles) -> None:
        if self.current_ultra_attack_cooldown <= 0:
            diagonal: float = max(distance_y, distance_x)
            projectiles.add(
                MagicBallEnemy(self.rect.centerx, self.rect.centery, distance_x, 0),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, 0, distance_y),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, -distance_x, 0),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, 0, -distance_y),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, diagonal, diagonal),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, -diagonal, diagonal),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, diagonal, -diagonal),
                MagicBallEnemy(self.rect.centerx, self.rect.centery, -diagonal, -diagonal)
            )
            self.current_ultra_attack_cooldown = self.ultra_attack_cooldown
        if self.current_attack_cooldown <= 0:
            projectile = MagicBallEnemy(self.rect.centerx, self.rect.centery, distance_x, distance_y)
            projectiles.add(projectile)
            self.current_attack_cooldown = self.attack_cooldown



