import pygame
from objects.interface_objects import Portal, PortalStand, Barrel, Coin
from structures_and_parameters.parameters_game import WindowParams


def get_portal_on_level(number_level: int):
    if number_level == 1:
        structures_by_room = {4: pygame.sprite.Group(
         PortalStand(), Portal()
        )}
    return structures_by_room


def get_structures_on_level(number_level: int):
    if number_level == 1:
        structures_by_room = {0: {"barrels": pygame.sprite.Group(
         Barrel(WindowParams.WIDTH//2-200, WindowParams.HEIGHT//2),
            Barrel(77, 77),
            Barrel(127, 77)
        ),
        "coins": pygame.sprite.Group(
                Coin(WindowParams.WIDTH // 2 + 300, WindowParams.HEIGHT // 2)
        )}
            ,
            8: {"barrels": pygame.sprite.Group(
         Barrel(WindowParams.WIDTH//2-200, WindowParams.HEIGHT//2)
        ),
        "coins": pygame.sprite.Group(
        )}
        }
    return structures_by_room

