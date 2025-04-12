import pygame
import random
from parameters_game import Color, WindowParams, Rooms


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width: int = 50
        self.height: int = 50
        self.image = pygame.Surface([self.width, self.height])
        self.image.fill(Color.VIOLET)
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 400
        self.speed_move: int = 5
        self.move_right = pygame.K_d
        self.move_left = pygame.K_a
        self.move_up = pygame.K_w
        self.move_down = pygame.K_s
        self.diagonal_move_rate: float = 0.7071
        self.speed_x: int = 0
        self.speed_y: int = 0
        self.room = 0
        self.can_change_room: bool = True
        # Rooms.LEVEL_ROOMS = level_map()

    def __generate_new_room(self, index: int):
        print(Rooms.LEVEL_ROOMS, Rooms.GENERATED_ROOM)
        if Rooms.CURRENT_ROOM in Rooms.LEVEL_ROOMS.keys():
            return Rooms.LEVEL_ROOMS[Rooms.CURRENT_ROOM]
        number_room: int = random.randint(1, Rooms.COUNT_ROOMS-1)
        while not (Rooms.rooms[number_room][index] == 1 and number_room not in Rooms.GENERATED_ROOM):
            number_room: int = random.randint(1, Rooms.COUNT_ROOMS-1)
        if Rooms.rooms[number_room].count(1) != 1:
            Rooms.GENERATED_ROOM.append(number_room)
        Rooms.LEVEL_ROOMS[Rooms.CURRENT_ROOM] = number_room
        return number_room

    def __next_room(self, door: str):
        if door == 'left':  # заходим в предыдущей комнате в правую дверь и выходим из левой
            self.speed_x = 0
            self.rect.left = 5
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord+1, y_coord)
            number_room: int = self.__generate_new_room(0)
        elif door == 'right':  # заходим в предыдущей комнате в левую дверь и выходим из правой
            self.speed_x = 0
            self.rect.right = WindowParams.WIDTH - 5
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord - 1, y_coord)
            number_room: int = self.__generate_new_room(2)
        elif door == 'top':  # заходим в предыдущей комнате в нижнюю дверь и выходим из верхней
            self.speed_y = 0
            self.rect.top = 5
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord, y_coord - 1)
            number_room: int = self.__generate_new_room(1)
        elif door == 'bottom':  # заходим в предыдущей комнате в верхнюю дверь и выходим из нижней
            self.speed_y = 0
            self.rect.bottom = WindowParams.HEIGHT - 5
            x_coord, y_coord = Rooms.CURRENT_ROOM
            Rooms.CURRENT_ROOM = (x_coord, y_coord + 1)
            number_room: int = self.__generate_new_room(3)
        Rooms.ROOM = number_room
        self.room += 1

    def __update_moves_player(self):
        moves_player = pygame.key.get_pressed()
        self.speed_x: int = 0
        self.speed_y: int = 0

        if moves_player[self.move_left] and moves_player[self.move_up]:
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
        elif moves_player[self.move_left] and moves_player[self.move_down]:
            self.speed_x = -self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
        elif moves_player[self.move_right] and moves_player[self.move_up]:
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = -self.speed_move * self.diagonal_move_rate
        elif moves_player[self.move_right] and moves_player[self.move_down]:
            self.speed_x = self.speed_move * self.diagonal_move_rate
            self.speed_y = self.speed_move * self.diagonal_move_rate
        elif moves_player[self.move_left]:
            self.speed_x = -self.speed_move
        elif moves_player[self.move_right]:
            self.speed_x = self.speed_move
        elif moves_player[self.move_up]:
            self.speed_y = -self.speed_move
        elif moves_player[self.move_down]:
            self.speed_y = self.speed_move

    # def __update_walls(self, walls):
    #     if self.rect.left < 0:
    #         self.__next_room('right')
    #     elif self.rect.right > WindowParams.WIDTH:
    #         self.__next_room('left')
    #     elif self.rect.top < 0:
    #         self.__next_room('bottom')
    #     elif self.rect.bottom > WindowParams.HEIGHT:
    #         self.__next_room('top')
    #
    #     self.rect.x += self.speed_x
    #     walls_collision = pygame.sprite.spritecollide(self, walls, False)
    #     for wall in walls_collision:
    #         if self.speed_x > 0:
    #             self.rect.right = wall.rect.left
    #         elif self.speed_x < 0:
    #             self.rect.left = wall.rect.right
    #         self.speed_x = 0
    #
    #     self.rect.y += self.speed_y
    #     walls_collision = pygame.sprite.spritecollide(self, walls, False)
    #     for wall in walls_collision:
    #         if self.speed_y > 0:
    #             self.rect.bottom = wall.rect.top
    #         elif self.speed_y < 0:
    #             self.rect.top = wall.rect.bottom
    #         self.speed_y = 0
    def __update_walls(self, walls):
        # Проверка перехода между комнатами
        if self.can_change_room:
            if self.rect.left < 0:
                self.__next_room('right')
                self.can_change_room = False
            elif self.rect.right > WindowParams.WIDTH:
                self.__next_room('left')
                self.can_change_room = False
            elif self.rect.top < 0:
                self.__next_room('bottom')
                self.can_change_room = False
            elif self.rect.bottom > WindowParams.HEIGHT:
                self.__next_room('top')
                self.can_change_room = False

        # Сброс флага, когда игрок ушёл от края
        margin = 10  # Порог для безопасной зоны, можно подогнать
        if (margin < self.rect.left < WindowParams.WIDTH - margin and
                margin < self.rect.top < WindowParams.HEIGHT - margin):
            self.can_change_room = True

        # Движение по X и проверка столкновений
        self.rect.x += self.speed_x
        walls_collision = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_collision:
            if self.speed_x > 0:
                self.rect.right = wall.rect.left
            elif self.speed_x < 0:
                self.rect.left = wall.rect.right
            self.speed_x = 0

        # Движение по Y и проверка столкновений
        self.rect.y += self.speed_y
        walls_collision = pygame.sprite.spritecollide(self, walls, False)
        for wall in walls_collision:
            if self.speed_y > 0:
                self.rect.bottom = wall.rect.top
            elif self.speed_y < 0:
                self.rect.top = wall.rect.bottom
            self.speed_y = 0

    def update(self, walls):
        self.__update_moves_player()
        self.__update_walls(walls)


class Walls(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.DARK_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Doors(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y