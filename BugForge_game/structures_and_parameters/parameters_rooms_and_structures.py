import pygame
from typing import Dict, List, Tuple
from objects.world_objects.world_structures import Portal, PortalStand, Doors, Tent
from objects.ui.text import TextOnWindowForOptions
from structures_and_parameters.parameters_game import WindowParams, ActionParams, Color
from structures_and_parameters.structures import get_structures


class Structures:
    """
    A class with a structure of levels, objects for each room, doors and tent
    """
    @staticmethod
    def get_doors() -> pygame.sprite.Group:
        doors = pygame.sprite.Group(
            Doors("vertical", x=2),
            Doors("vertical", x=WindowParams.WIDTH-2),
            Doors("horizontal", y=2),
            Doors("horizontal", y=WindowParams.HEIGHT-2)
        )
        return doors

    @staticmethod
    def get_level(number_level: int) -> Dict[tuple, int]:
        if number_level == 1:
            return {(0, 0): 0, (1, 0): 8, (1, 1): 4, (-1, 0): 1, (-1, 1): 11, (-1, -1): 12, (0, -1): 7, (-2, 0): 2,
                    (-2, 1): 9, (-2, -1): 5}
        if number_level == 2:
            return {(0, 0): 0, (1, 0): 11, (1, -1): 3, (1, -2): 12, (2, -2): 7, (-1, 0): 9, (-1, -1): 5}
        if number_level == 3:
            return {(0, 0): 0, (1, 0): 11, (1, -1): 5, (-1, 0): 12, (-1, 1): 9, (0, 1): 13, (1, 1): 7, (0, 2): 4}
        if number_level == 4:
            return {(0, 0): 3, (0, -1): 5, (0, 1): 4}

    @staticmethod
    def get_portal_on_level(number_level: int) -> Dict[int, pygame.sprite.Group]:
        print(number_level)
        if number_level == 1:
            structures_by_room = {4: pygame.sprite.Group(
                PortalStand(), Portal()
            )}
        if number_level == 2:
            structures_by_room = {7: pygame.sprite.Group(
                PortalStand(), Portal()
            )}
        if number_level == 3:
            structures_by_room = {4: pygame.sprite.Group(
                PortalStand(), Portal()
            )}
        if number_level == 4:
            structures_by_room = {}
        return structures_by_room

    @staticmethod
    def get_tent(number_level: int) -> Dict[int, pygame.sprite.Group]:
        if number_level == 1:
            tent_by_level = {5: pygame.sprite.Group(
                Tent()
            )}
        if number_level == 2:
            tent_by_level = {5: pygame.sprite.Group(
                Tent()
            )}
        if number_level == 3:
            tent_by_level = {7: pygame.sprite.Group(
                Tent()
            )}
        if number_level == 4:
            tent_by_level = {5: pygame.sprite.Group(
                Tent()
            )}
        return tent_by_level

    @staticmethod
    def get_structures_on_level(number_level: int) -> Dict[int, pygame.sprite.Group]:
        """
        The offset on the sides of each barrel is 68
        """
        return get_structures(number_level)


class Rooms:
    """
    Комнаты строятся по кортежам, каждый индекс картежа это наличие двери в нужную сторону лево -> вверх -> право -> низ
    """
    rooms: List[tuple] = [
        (1, 0, 1, 0),
        (1, 1, 1, 1),
        (0, 1, 1, 1),
        (0, 1, 0, 1),
        (0, 0, 0, 1),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (0, 0, 1, 1),
        (1, 0, 1, 1),
        (1, 0, 0, 1),
        (0, 1, 1, 0)
    ]
    COUNT_ROOMS: int = len(rooms)
    NUMBER_LEVEL: int = 1
    LEVEL_ROOMS: Dict[tuple, int] = Structures.get_level(NUMBER_LEVEL)
    LEVEL_STRUCTURE: Dict[int, dict] = Structures.get_structures_on_level(NUMBER_LEVEL)
    PORTAL_AND_STAND: Dict[int, pygame.sprite.Group] = Structures.get_portal_on_level(NUMBER_LEVEL)
    TENT: Dict[int, pygame.sprite.Group] = Structures.get_tent(NUMBER_LEVEL)
    ROOM: int = LEVEL_ROOMS[(0, 0)]
    DOORS = Structures.get_doors()
    DOORS_FLAG: bool = False
    CURRENT_ROOM: Tuple[int, int] = (0, 0)
    GENERATED_ROOM: List[int] = [0]
    FLAG_SWAP_LEVEL: bool = False
    FLAG_LOAD_SAVE: bool = False
    COST_UPDATE_DAMAGE: int = 200
    COST_UPDATE_SPEED: int = 150
    COST_UPDATE_RECOVERED_MANA: int = 200
    COST_RECOVERY_HEALTH: int = 200

    @staticmethod
    def fade_swap_level():
        surface = pygame.Surface(WindowParams.SCREEN.get_size())
        surface.fill(Color.BLACK)
        clock = pygame.time.Clock()
        steps = 30
        for i in range(0, 255, 255 // steps):
            surface.set_alpha(i)
            WindowParams.SCREEN.blit(surface, (0, 0))
            txt_surface = TextOnWindowForOptions(WindowParams.SCREEN.get_width() // 2,
                                                 WindowParams.SCREEN.get_height() // 2,
                                                 f"Уровень {Rooms.NUMBER_LEVEL}",
                                                 Color.WHITE,
                                                 96
            )
            txt_surface.draw_text(WindowParams.SCREEN)
            pygame.display.update()
            clock.tick(1000 // (ActionParams.DURATION_FADE_SWAP_LEVEL // steps))

    @staticmethod
    def update_level() -> None:
        Rooms.NUMBER_LEVEL += 1
        Rooms.fade_swap_level()
        Rooms.LEVEL_ROOMS = Structures.get_level(Rooms.NUMBER_LEVEL)
        Rooms.LEVEL_STRUCTURE = Structures.get_structures_on_level(Rooms.NUMBER_LEVEL)
        Rooms.PORTAL_AND_STAND = Structures.get_portal_on_level(Rooms.NUMBER_LEVEL)
        Rooms.TENT = Structures.get_tent(Rooms.NUMBER_LEVEL)
        Rooms.CURRENT_ROOM = (0, 0)
        Rooms.DOORS_FLAG = False
        Rooms.ROOM = Rooms.LEVEL_ROOMS[(0, 0)]
        Rooms.FLAG_SWAP_LEVEL = True
        Rooms.COST_UPDATE_DAMAGE += 50
        Rooms.COST_UPDATE_SPEED += 50
        Rooms.COST_UPDATE_RECOVERED_MANA += 50

    @staticmethod
    def restart_parameters() -> None:
        Rooms.DOORS_FLAG = False
        Rooms.NUMBER_LEVEL = Rooms.NUMBER_LEVEL if Rooms.FLAG_LOAD_SAVE else 1
        Rooms.CURRENT_ROOM = (0, 0)
        Rooms.LEVEL_ROOMS = Structures.get_level(Rooms.NUMBER_LEVEL)
        Rooms.LEVEL_STRUCTURE = Structures.get_structures_on_level(Rooms.NUMBER_LEVEL)
        Rooms.TENT = Structures.get_tent(Rooms.NUMBER_LEVEL)
        Rooms.ROOM = Rooms.LEVEL_ROOMS[(0, 0)]
        Rooms.COST_UPDATE_DAMAGE = 200
        Rooms.COST_UPDATE_SPEED = 150
        Rooms.COST_UPDATE_RECOVERED_MANA = 200
        ActionParams.RECOVERY_MANA_BAR = 3000

