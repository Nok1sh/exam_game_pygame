import pygame
import random
import math
from typing import Dict
from structures_and_parameters.parameters_game import Color, Textures, ActionParams
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from objects.world_objects.coin import Coin
from ..projectiles_direction.magic_balls_model import Projectile


class Enemy(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.width: int = 50
        self.height: int = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Color.RED)
        self.rect = self.image.get_rect()
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

    def update(self, player, walls, magic_balls, projectiles, moneys_group, barrels=None, columns=None) -> None:
        if self.current_health <= 0:
            self.kill()
        if self.current_ultra_attack_cooldown > 0:
            self.current_ultra_attack_cooldown -= 1
        if self.current_attack_cooldown > 0:
            self.current_attack_cooldown -= 1
        self.move_towards_player(player, walls)
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

    def move_towards_player(self, player, walls) -> None:
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
            if self.current_health <= 0:
                self.kill()
                if random.random() <= 0.2:
                    moneys_group.add(Coin(self.x, self.y))


class MeleeEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self, x, y)
        self.size_melee_enemy: int = 10
        self.image = pygame.image.load(f"textures/melee_enemy/melee_enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_melee_enemy, self.image.get_height()//self.size_melee_enemy))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.speed: int = 4
        self.push_distance: int = 2
        self.attack_damage: float = 0.5
        self.attack_range: int = 90
        self.number_image: int = 1
        self.animation_melee_enemy: int = 0
        self.speed_rotation: int = 40

    def swap_image(self):
        self.image = Textures.MELEE_ENEMY[self.number_image-1]
        self.image = pygame.transform.scale(self.image, (
        self.image.get_width() // self.size_melee_enemy, self.image.get_height() // self.size_melee_enemy))

    def move_towards_player(self, player, walls) -> None:
        self.animation_melee_enemy += ActionParams.TIME_ANIMATION_MELEE_ENEMY
        if self.animation_melee_enemy >= 1 / self.speed_rotation:
            self.animation_melee_enemy -= 1.0 / self.speed_rotation
            self.swap_image()
            self.number_image = self.number_image % 5 + 1
        distance_x: int = player.rect.x - self.rect.x
        distance_y: int = player.rect.y - self.rect.y
        distance: float = math.sqrt(distance_x**2 + distance_y**2)

        if distance > 0:
            distance_x /= distance
            distance_y /= distance

        if self.rect.colliderect(player.rect):
            self.rect.x -= distance_x * self.push_distance
            self.rect.y -= distance_y * self.push_distance
        else:
            new_x: float = self.rect.x + distance_x*self.speed
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


class RangeEnemy(Enemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        Enemy.__init__(self, x, y)
        self.size_range_enemy: int = 22
        self.image = pygame.image.load(f"textures/range_enemy/range_enemy_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_range_enemy, self.image.get_height() // self.size_range_enemy))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.distance_attack: int = 350
        self.evade_chance: float = 0.3
        self.attack_cooldown: float = 125
        self.number_image: int = 1
        self.animation_range_enemy: int = 0
        self.speed_rotation: int = 10

    def swap_image(self):
        self.image = Textures.RANGE_ENEMY[self.number_image-1]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_range_enemy, self.image.get_height() // self.size_range_enemy))

    def move_towards_player(self, player, walls) -> None:
        self.animation_range_enemy += ActionParams.TIME_ANIMATION_MELEE_ENEMY
        if self.animation_range_enemy >= 1 / self.speed_rotation:
            self.animation_range_enemy -= 1.0 / self.speed_rotation
            self.swap_image()
            self.number_image = self.number_image % 26 + 1

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
            projectile = Projectile(self.rect.centerx, self.rect.centery, distance_x, distance_y)
            projectiles.add(projectile)
            self.current_attack_cooldown = self.attack_cooldown


class RangeBossEnemy(RangeEnemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        RangeEnemy.__init__(self, x, y)
        self.width: int = 70
        self.height: int = 70
        self.size_boss_range_enemy: int = 10
        self.image = pygame.image.load(f"textures/boss_range_enemy/boss_range_enemy1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_boss_range_enemy, self.image.get_height() // self.size_boss_range_enemy))
        self.rect = self.image.get_rect()
        self.x: int = x
        self.y: int = y
        self.rect.x = x
        self.rect.y = y
        self.image.fill(Color.YELLOW)
        self.speed: int = 2
        self.ultra_attack_cooldown: int = 175
        self.distance_attack: int = 500
        self.max_health: float = 25
        self.current_health: float = self.max_health
        self.number_image: int = 1
        self.animation_range_enemy: int = 0
        self.speed_rotation: int = 10

    def swap_image(self):
        self.image = Textures.BOSS_RANGE_ENEMY[self.number_image - 1]
        self.image = pygame.transform.scale(self.image, (
        self.image.get_width() // self.size_boss_range_enemy, self.image.get_height() // self.size_boss_range_enemy))

    def move_towards_player(self, player, walls) -> None:
        self.animation_range_enemy += ActionParams.TIME_ANIMATION_MELEE_ENEMY
        if self.animation_range_enemy >= 1 / self.speed_rotation:
            self.animation_range_enemy -= 1.0 / self.speed_rotation
            self.swap_image()
            self.number_image = self.number_image % 24 + 1

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
                Projectile(self.rect.centerx, self.rect.centery, distance_x, 0),
                Projectile(self.rect.centerx, self.rect.centery, 0, distance_y),
                Projectile(self.rect.centerx, self.rect.centery, -distance_x, 0),
                Projectile(self.rect.centerx, self.rect.centery, 0, -distance_y),
                Projectile(self.rect.centerx, self.rect.centery, diagonal, diagonal),
                Projectile(self.rect.centerx, self.rect.centery, -diagonal, diagonal),
                Projectile(self.rect.centerx, self.rect.centery, diagonal, -diagonal),
                Projectile(self.rect.centerx, self.rect.centery, -diagonal, -diagonal)
            )
            self.current_ultra_attack_cooldown = self.ultra_attack_cooldown
        if self.current_attack_cooldown <= 0:
            projectile = Projectile(self.rect.centerx, self.rect.centery, distance_x, distance_y)
            projectiles.add(projectile)
            self.current_attack_cooldown = self.attack_cooldown