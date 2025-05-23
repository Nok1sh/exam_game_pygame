import pygame
from structures_and_parameters.enemies_on_each_levels import GetEnemiesStructure
from objects.action_objects import Player, MagicBall
from objects.interface_objects import ManaBar, HealthBar, Portal, PortalStand, Floor, MoneyBar, TextOnWindowForGame
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
    for magic_ball in magic_balls:
        magic_ball.kill()
