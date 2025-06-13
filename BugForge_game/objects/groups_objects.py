import pygame
from structures_and_parameters.groups_of_enemies_model import GetEnemiesStructure
from objects.action_objects.projectiles_direction.magic_balls import MagicBallPlayer
from .action_objects.player_direction.player_model import Player
from .action_objects.player_direction.player_render import PlayerRender
from objects.world_objects.world_structures import Portal, PortalStand
from .ui.bars import MoneyBar, ManaBar, HealthBar
from .ui.text import TextOnWindowForGame
from structures_and_parameters.rooms import room_number

buttons_main_menu_group = pygame.sprite.Group()

player_group = pygame.sprite.Group(
    Player()
)

player_render_group = pygame.sprite.Group(
    PlayerRender()
)

def walls_group(number: int):
    walls = room_number(number)
    return walls


player = next(iter(player_group))
magic_balls_hero = pygame.sprite.Group()


def add_magic_ball(line_move: str, center: tuple):
    magic_balls_hero.add(
        MagicBallPlayer(center, line_move)
    )


bars = pygame.sprite.Group(
    ManaBar(player),
    HealthBar(player),
    MoneyBar()
)

magic_ball_enemy = pygame.sprite.Group()

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
    magic_balls_hero.empty()
    magic_ball_enemy.empty()
