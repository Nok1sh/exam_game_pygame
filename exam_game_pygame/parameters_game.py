from typing import Tuple, List, Dict
import random


class WindowParams:
    WIDTH: int = 1000
    HEIGHT: int = 800
    FPS: int = 60


class Color:
    WHITE: Tuple[int] = (255, 255, 255)
    RED: Tuple[int] = (255, 0, 0)
    GREEN: Tuple[int] = (0, 255, 0)
    DARK_GREEN: Tuple[int] = (0, 100, 0)
    BLUE: Tuple[int] = (0, 0, 255)
    BLACK: Tuple[int] = (0, 0, 0)
    YELLOW: Tuple[int] = (255, 255, 0)
    VIOLET: Tuple[int] = (128, 0, 128)
    ORANGE: Tuple[int] = (255, 165, 0)
    PINK: Tuple[int] = (255, 192, 203)
    GRAY: Tuple[int] = (128, 128, 128)
    TURQUOISE: Tuple[int] = (64, 224, 208)


class Rooms:
    """
    Комнаты строятся по кортежам, каждый индекс картежа это наличие двери в нужную сторону лево -> вверх -> право -> низ
    """
    ROOM: int = 0
    rooms: List[tuple] = [
        (1, 0, 1, 0),
        (1, 1, 1, 1),
        (0, 1, 1, 1),
        (0, 1, 0, 1),
        (0, 0, 0, 1),
        (0, 1, 0, 0),
        (0, 0, 1, 0),
        (1, 0, 0, 0)
    ]
    COUNT_ROOMS: int = len(rooms)
    LEVEL_ROOMS: Dict[tuple, int] = {(0, 0): 0,}

    CURRENT_ROOM: Tuple[int, int] = (0, 0)
    GENERATED_ROOM: List[int] = [0]

    # @classmethod
    # def generate_new_room(cls, index: int):
    #     print(cls.LEVEL_ROOMS)
    #     if cls.CURRENT_ROOM in cls.LEVEL_ROOMS.keys():
    #         return cls.LEVEL_ROOMS[cls.CURRENT_ROOM]
    #     if len(Rooms.GENERATED_ROOM) != cls.COUNT_ROOMS:
    #         number_room: int = random.randint(1, cls.COUNT_ROOMS-1)
    #         while not (cls.rooms[number_room][index] == 1 and number_room not in cls.GENERATED_ROOM):
    #             number_room: int = random.randint(1, cls.COUNT_ROOMS-1)
    #         cls.GENERATED_ROOM.append(number_room)
    #         cls.LEVEL_ROOMS[cls.CURRENT_ROOM] = number_room
    #         return number_room
