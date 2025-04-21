import pygame
from parameters_game import Rooms
from action_objects import Player, MagicBall
from interface_objects import ManaBar, HealthBar, ButtonMainMenu
from room_structures import room_number
from enemies_on_each_levels import get_enemies_on_level


buttons_main_menu_group = pygame.sprite.Group()

player_group = pygame.sprite.Group(
    Player()
)


def walls_group(number: int):
    walls = room_number(number)
    return walls


player = next(iter(player_group))
magic_balls = pygame.sprite.Group()


def add_magic_ball(line_move: str, x: int, y: int):
    magic_balls.add(
        MagicBall(x, y, line_move)
    )


bars = pygame.sprite.Group(
    ManaBar(player),
    HealthBar(player)
)

projectiles = pygame.sprite.Group()

enemies_by_room = get_enemies_on_level(Rooms.NUMBER_LEVEL)

