import pygame
from interface_objects import Portal, PortalStand


def get_structures_on_level(number_level: int):
    if number_level == 1:
        structures_by_room = {4: pygame.sprite.Group(
         PortalStand(), Portal()
        )}
    return structures_by_room