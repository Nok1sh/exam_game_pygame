import pygame
import time
from typing import Dict
from structures_and_parameters.parameters_game import WindowParams, Textures, ActionParams
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from game_windows.window_options import store_menu


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width: int = 50
        self.height: int = 50
        self.size_width: int = 9
        self.size_height: int = 8
        self.image = pygame.image.load("textures/hero/hero.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_width, self.image.get_height()//self.size_height))
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
        self.max_health: int = 4 if ActionParams.FLAG_UPPER_HEALTH_BAR else 3
        self.max_mana: int = 5
        self.mana_pool: int = self.max_mana
        self.health_bar: float = self.max_health
        self.flag_swap_health_bar: bool = False if ActionParams.FLAG_UPPER_HEALTH_BAR else True
        self.damage: float = 1.5
        self.is_life: bool = True
        self.score: int = 0
        self.health_potion: int = 1
        self.mana_potion: int = 3
        self.animation_lines: Dict[str, int] = {
            "top": 1, "right_top": 3, "right": 5, "bottom": 7, "left_top": 9,
            "right_bottom": 11, "left_bottom": 13, "left": 15
        }
        self.animation_moves: Dict[str, int] = {
            "top": 0, "right_top": 0, "right": 0, "bottom": 0, "left_top": 0,
            "right_bottom": 0, "left_bottom": 0, "left": 0
        }
        self.animation_lines_constant: Dict[str, tuple] = {
            "top": (1, 2), "right_top": (3, 4), "right": (5, 6), "bottom": (7, 8), "left_top": (9, 10),
            "right_bottom": (11, 12), "left_bottom": (13, 14), "left": (15, 16)
        }
        self.speed_animation: int = 10
        self.animation_move: int = 0

    def restart_parameters(self) -> None:
        """
        Updating changing settings when restarting the game
        """
        self.rect.x = WindowParams.WIDTH // 2
        self.rect.y = WindowParams.HEIGHT // 2
        self.speed_x: int = 0
        self.speed_y: int = 0
        self.speed_move: int = self.speed_move if Rooms.FLAG_LOAD_SAVE else 5
        self.damage: float = self.damage if Rooms.FLAG_LOAD_SAVE else 1.5
        self.mana_pool: int = self.max_mana
        if not Rooms.FLAG_LOAD_SAVE:
            self.health_bar: int = 4 if ActionParams.FLAG_UPPER_HEALTH_BAR else 3
            self.flag_swap_health_bar: bool = False if ActionParams.FLAG_UPPER_HEALTH_BAR else True
        self.score: int = self.score if Rooms.FLAG_LOAD_SAVE else 0
        self.is_life: bool = True
        Rooms.restart_parameters()

    @staticmethod
    def __generate_new_room() -> int:
        """
        Getting the room number based on the character's coordinate
        """
        if Rooms.CURRENT_ROOM in Rooms.LEVEL_ROOMS.keys():
            return Rooms.LEVEL_ROOMS[Rooms.CURRENT_ROOM]

    def __next_room(self, door: str) -> None:
        """
        Handling the movement of the hero between rooms
        """
        if door == 'left':  # заходим в предыдущей комнате в правую дверь и выходим из левой
            self.speed_x = 0
            self.rect.left = 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord+1, y_coord)
            number_room: int = self.__generate_new_room()
        elif door == 'right':  # заходим в предыдущей комнате в левую дверь и выходим из правой
            self.speed_x = 0
            self.rect.right = WindowParams.WIDTH - 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord - 1, y_coord)
            number_room: int = self.__generate_new_room()
        elif door == 'top':  # заходим в предыдущей комнате в нижнюю дверь и выходим из верхней
            self.speed_y = 0
            self.rect.top = 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord, y_coord - 1)
            number_room: int = self.__generate_new_room()
        elif door == 'bottom':  # заходим в предыдущей комнате в верхнюю дверь и выходим из нижней
            self.speed_y = 0
            self.rect.bottom = WindowParams.HEIGHT - 15
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord, y_coord + 1)
            number_room: int = self.__generate_new_room()
        Rooms.ROOM = number_room

    def __swap_image(self, number: int, line: str) -> None:
        """
        Changing the image of the hero when moving
        """
        self.image = Textures.PLAYER[number-1]
        if line == "horizontal":
            self.image = Textures.PLAYER_HORIZONTAL[number]
        elif line == "vertical":
            self.image = Textures.PLAYER_VERTICAL[number]
        else:
            self.image = Textures.PLAYER_DIAGONAL[number]

    def __animation_move_hero(self, line: str, direction: str) -> None:
        """
        Handling hero animation when moving
        """
        self.animation_moves[line] += ActionParams.TIME_ANIMATION_HERO_MOVE
        if self.animation_moves[line] >= 1 / self.speed_animation:
            self.animation_moves[line] -= 1.0 / self.speed_animation
            self.__swap_image(self.animation_lines[line], direction)
            self.animation_lines[line] = self.animation_lines_constant[line][1] \
                if self.animation_lines[line] == self.animation_lines_constant[line][0] \
                else self.animation_lines_constant[line][0]

    def __update_moves_player(self) -> None:
        moves_player = pygame.key.get_pressed()
        self.speed_x: int = 0
        self.speed_y: int = 0

        if moves_player[self.move_left] and moves_player[self.move_up]:
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
            self.line_move = 'left_top'
            self.__animation_move_hero("left_top", "diagonal")
        elif moves_player[self.move_left] and moves_player[self.move_down]:
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
            self.line_move = 'left_bottom'
            self.__animation_move_hero("left_bottom", "diagonal")
        elif moves_player[self.move_right] and moves_player[self.move_up]:
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
            self.line_move = 'right_top'
            self.__animation_move_hero("right_top", "diagonal")
        elif moves_player[self.move_right] and moves_player[self.move_down]:
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
            self.line_move = 'right_bottom'
            self.__animation_move_hero("right_bottom", "diagonal")
        elif moves_player[self.move_left]:
            self.speed_x = -self.speed_move
            self.line_move = 'left'
            self.__animation_move_hero("left", "horizontal")
        elif moves_player[self.move_right]:
            self.speed_x = self.speed_move
            self.line_move = 'right'
            self.__animation_move_hero("right", "horizontal")
        elif moves_player[self.move_up]:
            self.speed_y = -self.speed_move
            self.line_move = 'top'
            self.__animation_move_hero("top", "vertical")
        elif moves_player[self.move_down]:
            self.speed_y = self.speed_move
            self.line_move = 'bottom'
            self.__animation_move_hero("bottom", "vertical")

    def __update_walls(self, walls) -> None:
        size_door: int = 75
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
                    current_health = self.health_bar + self.health_potion
                    if current_health >= self.max_health:
                        current_health = self.max_health
                    self.health_bar = current_health
                elif potion.name == "mana":
                    current_mana = self.mana_pool + self.mana_potion
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