import pygame
from structures_and_parameters.enemies_on_each_levels import GetEnemiesStructure
from objects.action_objects.projectiles_direction.magic_balls_model import MagicBall
from .action_objects.player_direction.player_model import Player
from objects.world_objects.world_structures import Portal, PortalStand
from .ui.bars import MoneyBar, ManaBar, HealthBar
from .ui.text import TextOnWindowForGame
from structures_and_parameters.rooms import room_number

buttons_main_menu_group = pygame.sprite.Group()

player_group = pygame.sprite.Group(
    Player()
)


def walls_group(number: int):
    walls = room_number(number)
    return walls


player = next(iter(player_group))
magic_balls = pygame.sprite.Group()


def add_magic_ball(line_move: str, center: tuple):
    magic_balls.add(
        MagicBall(center, line_move)
    )


bars = pygame.sprite.Group(
    ManaBar(player),
    HealthBar(player),
    MoneyBar()
)

projectiles = pygame.sprite.Group()

portal = pygame.sprite.Group(
    Portal()
)

portal_stand = pygame.sprite.Group(
    PortalStand()
)


text_score_money = TextOnWindowForGame(85, 15)


def restart_game():
    player.restart_parameters()
    GetEnemiesStructure.restart_game()
    magic_balls.empty()
    projectiles.empty()
