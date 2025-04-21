import pygame
from action_objects import MeleeEnemy, RangeEnemy

def get_enemies_on_level(number_level: int):
    if number_level == 1:
        enemies_by_room = {1: pygame.sprite.Group(
            RangeEnemy()
        ),
            2: pygame.sprite.Group(
                MeleeEnemy()
            ),
            8: pygame.sprite.Group(
                MeleeEnemy()
            )}
    return enemies_by_room
