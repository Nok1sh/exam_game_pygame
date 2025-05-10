import pygame
import random
from structures_and_parameters.parameters_game import Color, WindowParams, Textures, ActionParams
from structures_and_parameters.structures_on_each_level import Rooms
from objects.interface_objects import Coin
from game_windows.window_options import store_menu
import time
import math


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width: int = 50
        self.height: int = 50
        #self.image = pygame.Surface([self.width, self.height])
        self.image = pygame.image.load("../exam_game_pygame/textures/hero/hero.png").convert_alpha()
        #self.image.fill(Color.VIOLET)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//7, self.image.get_height()//7))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2)
        self.speed_move: int = 5
        self.move_right = pygame.K_d
        self.move_left = pygame.K_a
        self.move_up = pygame.K_w
        self.move_down = pygame.K_s
        self.interaction_with_objects = pygame.K_e
        self.line_move: str = 'right'  # right, left, top, bottom, right_top, right_bottom, left_top, left_bottom
        self.diagonal_move_rate: float = 0.7071
        self.speed_x: int = 0
        self.speed_y: int = 0
        self.can_change_room: bool = True
        self.time_next_room = time.time()
        self.max_health: int = 3
        self.max_mana: int = 5
        self.mana_pool: int = self.max_mana
        self.health_bar: float = self.max_health
        self.damage: float = 1.5
        self.is_life: bool = True
        self.score: int = 0
        self.animation_top = 1
        self.animation_right_top = 3
        self.animation_right = 5
        self.animation_bottom = 7
        self.animation_left_top = 9
        self.animation_right_bottom = 11
        self.animation_left_bottom = 13
        self.animation_left = 15
        self.speed_animation = 10
        self.animation_move = 0

    def restart_parameters(self) -> None:
        self.rect.x = WindowParams.WIDTH // 2
        self.rect.y = WindowParams.HEIGHT // 2
        self.speed_x: int = 0
        self.speed_y: int = 0
        self.speed_move: int = 5
        self.damage: float = 1.5
        self.mana_pool: int = 5
        self.health_bar: int = 3
        self.score: int = 0
        self.is_life: bool = True
        Rooms.restart_parameters()

    @staticmethod
    def __generate_new_room(index: int) -> int:
        if Rooms.CURRENT_ROOM in Rooms.LEVEL_ROOMS.keys():
            return Rooms.LEVEL_ROOMS[Rooms.CURRENT_ROOM]
        # number_room: int = random.randint(1, Rooms.COUNT_ROOMS-1)
        # while not (Rooms.rooms[number_room][index] == 1 and number_room not in Rooms.GENERATED_ROOM):
        #     number_room: int = random.randint(1, Rooms.COUNT_ROOMS-1)
        # if Rooms.rooms[number_room].count(1) != 1:
        #     Rooms.GENERATED_ROOM.append(number_room)
        # Rooms.LEVEL_ROOMS[Rooms.CURRENT_ROOM] = number_room
        # return number_room

    def __next_room(self, door: str) -> None:
        if door == 'left':  # заходим в предыдущей комнате в правую дверь и выходим из левой
            self.speed_x = 0
            self.rect.left = 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord+1, y_coord)
            number_room: int = self.__generate_new_room(0)
        elif door == 'right':  # заходим в предыдущей комнате в левую дверь и выходим из правой
            self.speed_x = 0
            self.rect.right = WindowParams.WIDTH - 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord - 1, y_coord)
            number_room: int = self.__generate_new_room(2)
        elif door == 'top':  # заходим в предыдущей комнате в нижнюю дверь и выходим из верхней
            self.speed_y = 0
            self.rect.top = 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord, y_coord - 1)
            number_room: int = self.__generate_new_room(1)
        elif door == 'bottom':  # заходим в предыдущей комнате в верхнюю дверь и выходим из нижней
            self.speed_y = 0
            self.rect.bottom = WindowParams.HEIGHT - 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord, y_coord + 1)
            number_room: int = self.__generate_new_room(3)
        Rooms.ROOM = number_room

    def __update_moves_player(self) -> None:
        moves_player = pygame.key.get_pressed()
        self.speed_x: int = 0
        self.speed_y: int = 0

        if moves_player[self.move_left] and moves_player[self.move_up]:
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
            self.line_move = 'left_top'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(
                    f"../exam_game_pygame/textures/hero/hero_move{self.animation_left_top}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_left_top = 10 if self.animation_left_top == 9 else 9
        elif moves_player[self.move_left] and moves_player[self.move_down]:
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
            self.line_move = 'left_bottom'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(
                    f"../exam_game_pygame/textures/hero/hero_move{self.animation_left_bottom}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_left_bottom = 14 if self.animation_left_bottom == 13 else 13
        elif moves_player[self.move_right] and moves_player[self.move_up]:
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
            self.line_move = 'right_top'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(
                    f"../exam_game_pygame/textures/hero/hero_move{self.animation_right_top}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_right_top = 4 if self.animation_right_top == 3 else 3
        elif moves_player[self.move_right] and moves_player[self.move_down]:
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
            self.line_move = 'right_bottom'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(
                    f"../exam_game_pygame/textures/hero/hero_move{self.animation_right_bottom}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_right_bottom = 12 if self.animation_right_bottom == 11 else 11
        elif moves_player[self.move_left]:
            self.speed_x = -self.speed_move
            self.line_move = 'left'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(
                    f"../exam_game_pygame/textures/hero/hero_move{self.animation_left}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_left = 16 if self.animation_left == 15 else 15
        elif moves_player[self.move_right]:
            self.speed_x = self.speed_move
            self.line_move = 'right'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(f"../exam_game_pygame/textures/hero/hero_move{self.animation_right}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_right = 6 if self.animation_right == 5 else 5
        elif moves_player[self.move_up]:
            self.speed_y = -self.speed_move
            self.line_move = 'top'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(f"../exam_game_pygame/textures/hero/hero_move{self.animation_top}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_top = 2 if self.animation_top == 1 else 1
        elif moves_player[self.move_down]:
            self.speed_y = self.speed_move
            self.line_move = 'bottom'
            self.animation_move += ActionParams.TIME_ANIMATION_HERO_MOVE
            if self.animation_move >= 1 / self.speed_animation:
                print(1)
                self.animation_move -= 1.0 / self.speed_animation
                self.image = pygame.image.load(
                    f"../exam_game_pygame/textures/hero/hero_move{self.animation_bottom}.png").convert_alpha()
                self.image = pygame.transform.scale(self.image,
                                                    (self.image.get_width() // 7, self.image.get_height() // 7))
                self.animation_bottom = 8 if self.animation_bottom == 7 else 7

    def __update_walls(self, walls) -> None:
        size_door = 75
        if time.time() - self.time_next_room > 0.5:
            self.time_next_room = time.time()
            if self.rect.left < 0:
                if self.rect.y in range(WindowParams.HEIGHT//2-size_door, WindowParams.HEIGHT//2+size_door):
                    self.__next_room('right')
            elif self.rect.right > WindowParams.WIDTH and self.rect.y in range(WindowParams.HEIGHT//2-size_door, WindowParams.HEIGHT//2+size_door):
                self.__next_room('left')
            elif self.rect.top < 0 and self.rect.x in range(WindowParams.WIDTH//2-size_door-25, WindowParams.WIDTH//2+size_door+25):
                self.__next_room('bottom')
            elif self.rect.bottom > WindowParams.HEIGHT and self.rect.x in range(WindowParams.WIDTH//2-size_door-25, WindowParams.WIDTH//2+size_door+25):
                self.__next_room('top')
        else:
            if self.rect.left < 0:
                self.rect.left = 0
            elif self.rect.right > WindowParams.WIDTH:
                self.rect.right = WindowParams.WIDTH
            elif self.rect.top < 0:
                self.rect.top = 0
            elif self.rect.bottom > WindowParams.HEIGHT:
                self.rect.bottom = WindowParams.HEIGHT

        self.rect.x += self.speed_x
        walls_collision = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_collision:
            if self.speed_x > 0:
                self.rect.right = wall.rect.left
            elif self.speed_x < 0:
                self.rect.left = wall.rect.right
            self.speed_x = 0

        self.rect.y += self.speed_y
        walls_collision = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_collision:
            if self.speed_y > 0:
                self.rect.bottom = wall.rect.top
            elif self.speed_y < 0:
                self.rect.top = wall.rect.bottom
            self.speed_y = 0

    def __update_portal(self, portal) -> None:
        interaction_player = pygame.key.get_pressed()
        collision_x = pygame.sprite.spritecollide(self, portal, False)
        for obj in collision_x:
            if self.speed_x > 0:
                self.rect.right = obj.rect.left
            elif self.speed_x < 0:
                self.rect.left = obj.rect.right
            self.speed_x = 0
            if interaction_player[self.interaction_with_objects]:
                Rooms.update_level()
                self.rect.x = WindowParams.WIDTH // 2
                self.rect.y = WindowParams.HEIGHT // 2

        collision_y = pygame.sprite.spritecollide(self, portal, False)
        for obj in collision_y:
            if self.speed_y > 0:
                self.rect.bottom = obj.rect.top
            elif self.speed_y < 0:
                self.rect.top = obj.rect.bottom
            self.speed_y = 0
            if interaction_player[self.interaction_with_objects]:
                Rooms.update_level()
                self.rect.x = WindowParams.WIDTH // 2
                self.rect.y = WindowParams.HEIGHT // 2

    def __update_structures(self, barrels, flag_tent=False, player=None) -> None:
        collided_structures = pygame.sprite.spritecollide(self, barrels, False)

        for barrel in collided_structures:
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
            if flag_tent:
                interaction_player = pygame.key.get_pressed()
                if interaction_player[self.interaction_with_objects]:
                    store_menu(player)

    def __update_moneys(self, moneys) -> None:
        moneys_collision = pygame.sprite.spritecollide(self, moneys, False)
        for coin in moneys_collision:
            if self.rect.collidepoint(coin.rect.center):
                self.score += coin.score
                coin.kill()

    def __update_potions(self, potion) -> None:
        potions_collision = pygame.sprite.spritecollide(self, potion, False)
        for potion in potions_collision:
            if self.rect.collidepoint(potion.rect.center):
                if potion.name == "health":
                    current_health = self.health_bar + 1
                    if current_health >= self.max_health:
                        current_health = self.max_health
                    self.health_bar = current_health
                elif potion.name == "mana":
                    current_mana = self.mana_pool + 2
                    if current_mana >= self.max_mana:
                        current_mana = self.max_mana
                    self.mana_pool = current_mana
                potion.kill()

    def take_damage(self, damage: float) -> None:
        self.health_bar -= damage
        if self.health_bar <= 0:
            self.is_life = False

    def update(self, player, walls=None, portal=None, barrels=None, moneys=None, columns=None, potions=None, tent=None) -> None:
        self.__update_moves_player()
        if potions:
            self.__update_potions(potions)
        if tent:
            self.__update_structures(tent, flag_tent=True, player=player)
        if Rooms.DOORS_FLAG:
            self.__update_structures(Rooms.DOORS)
        if barrels:
            self.__update_structures(barrels)
        if columns:
            self.__update_structures(columns)
        if walls:
            self.__update_walls(walls)
        if portal:
            self.__update_portal(portal)
        if moneys:
            self.__update_moneys(moneys)


class MagicBall(pygame.sprite.Sprite):
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
        self.max_health: int = 3
        self.current_health: int = self.max_health
        self.attack_cooldown: float = 250
        self.current_attack_cooldown: float = 50
        self.attack_range: int = 55

    def update(self, player, walls, magic_balls, projectiles, moneys_group, barrels=None, columns=None) -> None:
        if self.current_health <= 0:
            self.kill()
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
        self.speed: int = 5
        self.min_chase_distance: int = 30
        self.push_distance: int = 2
        self.attack_damage: float = 0.5
        self.attack_range: int = 55

    def move_towards_player(self, player, walls) -> None:
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
        self.distance_attack: int = 350
        self.evade_chance: float = 0.3
        self.attack_cooldown: float = 125
        self.image.fill(Color.PINK)

    def move_towards_player(self, player, walls) -> None:
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


class Projectile(RangeEnemy, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, distance_x: float, distance_y: float):
        pygame.sprite.Sprite.__init__(self)
        self.attack_damage: float = 1
        self.projectile_speed: float = 7
        self.image = pygame.Surface((15, 15))
        self.image.fill(Color.WHITE)
        self.rect = self.image.get_rect(center=(x, y))
        self.line_attack = math.sqrt(distance_x**2 + distance_y**2)
        self.velocity_x: float = self.projectile_speed * (distance_x/self.line_attack)
        self.velocity_y: float = self.projectile_speed * (distance_y/self.line_attack)

    def update(self, current_enemies, player, walls, barrels=None, columns=None) -> None:
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y
        if self.rect.colliderect(player.rect):
            player.take_damage(self.attack_damage)
            self.kill()

        elif not (0 < self.rect.center[0] < WindowParams.WIDTH) or not (0 < self.rect.center[1] < WindowParams.HEIGHT):
            self.kill()
        elif pygame.sprite.spritecollide(self, walls, False) or pygame.sprite.spritecollide(self, barrels, False) or \
                pygame.sprite.spritecollide(self, columns, False) or not current_enemies:
            self.kill()

