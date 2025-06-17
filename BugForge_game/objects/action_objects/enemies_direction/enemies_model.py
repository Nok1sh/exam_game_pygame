import pygame
import random
from structures_and_parameters.parameters_game import Color
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from objects.world_objects.coin import Coin


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.width: int = 50
        self.height: int = 50
        self.width_collision: int = 55
        self.height_collision: int = 55
        self.rect = pygame.Rect(
            x,
            y,
            self.width_collision,
            self.height_collision
        )
        self.x: int = x
        self.y: int = y
        self.rect.x = x
        self.rect.y = y
        self.speed: int = 3
        self.max_health: float = 3 + (Rooms.NUMBER_LEVEL-1) * 0.5
        self.current_health: float = self.max_health
        self.attack_cooldown: int = 250
        self.current_attack_cooldown: int = 50
        self.current_ultra_attack_cooldown: int = 250
        self.attack_range: int = 55
        self.render_enemy = ...

    def update(self, player, walls, magic_balls, projectiles, moneys_group, barrels=None, columns=None) -> None:
        self.render_enemy.update()
        if self.current_health <= 0:
            self.kill()
        if self.current_ultra_attack_cooldown > 0:
            self.current_ultra_attack_cooldown -= 1
        if self.current_attack_cooldown > 0:
            self.current_attack_cooldown -= 1
        self.move_towards_enemy(player, walls)
        self.check_attack(player, projectiles)
        self.take_damage(magic_balls, player, moneys_group)
        if barrels:
            self.__update_barrels(barrels)
        if columns:
            self.__update_barrels(columns)

    def __update_barrels(self, barrels) -> None:
        collided_barrels = pygame.sprite.spritecollide(self, barrels, False)

        for barrel in collided_barrels:
            dx = (self.rect.centerx - barrel.rect.centerx) / (barrel.rect.width / 2)
            dy = (self.rect.centery - barrel.rect.centery) / (barrel.rect.height / 2)

            if abs(dx) > abs(dy):
                if dx > 0:
                    self.rect.left = barrel.rect.right
                else:
                    self.rect.right = barrel.rect.left
            else:
                if dy > 0:
                    self.rect.top = barrel.rect.bottom
                else:
                    self.rect.bottom = barrel.rect.top

    def move_towards_enemy(self, player, walls) -> None:
        pass

    def can_move(self, new_x: float, new_y: float, walls) -> bool:
        new_rect = self.rect.copy()
        new_rect.x = new_x
        new_rect.y = new_y

        for wall in walls:
            if new_rect.colliderect(wall.rect):
                return False
        return True

    def check_attack(self, player, projectiles) -> None:
        pass

    def attack(self, player, distance_x: float, distance_y: float, projectiles) -> None:
        pass

    def take_damage(self, magic_balls, player, moneys_group) -> None:
        balls_collision = pygame.sprite.spritecollide(self, magic_balls, True)
        if balls_collision:
            self.current_health -= player.damage
            print(self.current_health)
            if self.current_health <= 0:
                self.kill()
                if random.random() <= 0.2:
                    moneys_group.add(Coin(self.x, self.y))
