import pygame
from structures_and_parameters.parameters_game import Rooms
from objects.action_objects import Player, MagicBall
from objects.interface_objects import ManaBar, HealthBar, Portal, PortalStand, Floor, MoneyBar, TextOnWindowForGame
from structures_and_parameters.room_structures import room_number
from structures_and_parameters.enemies_on_each_levels import get_enemies_on_level
from structures_and_parameters.structures_on_each_level import get_portal_on_level, get_structures_on_level

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
    HealthBar(player),
    MoneyBar(player)
)

projectiles = pygame.sprite.Group()

enemies_by_room = get_enemies_on_level(Rooms.NUMBER_LEVEL)

portal_and_stand = get_portal_on_level(Rooms.NUMBER_LEVEL)

other_structures = get_structures_on_level(Rooms.NUMBER_LEVEL)

portal = pygame.sprite.Group(
    Portal()
)

portal_stand = pygame.sprite.Group(
    PortalStand()
)


text_score_money = TextOnWindowForGame(85, 15)


def restart_game():
    global enemies_by_room, other_structures
    player.restart_parameters()
    for magic_ball in magic_balls:
        magic_ball.kill()
    return get_enemies_on_level(Rooms.NUMBER_LEVEL), get_structures_on_level(Rooms.NUMBER_LEVEL)
