import pygame
from structures_and_parameters.parameters_game import WindowParams
from objects.action_objects import MeleeEnemy, RangeEnemy


def get_enemies_on_level(number_level: int):
    if number_level == 1:
        enemies_by_room = {1: pygame.sprite.Group(
            RangeEnemy(100, 100)
        ),
            2: pygame.sprite.Group(
                MeleeEnemy(200, WindowParams.HEIGHT//2)
            ),
            8: pygame.sprite.Group(
                MeleeEnemy(WindowParams.WIDTH//2, WindowParams.HEIGHT//2)
            )}
    return enemies_by_room
