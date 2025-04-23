import pygame
from levels import get_level
from typing import Tuple, List, Dict
pygame.init()


class WindowParams:
    info = pygame.display.Info()
    WIDTH: int = int(info.current_w*0.8)
    HEIGHT: int = int(info.current_h*0.8)
    SCREEN_WIDTH: int = WIDTH
    SCREEN_HEIGHT: int = HEIGHT
    # WIDTH: int = 1000
    # HEIGHT: int = 800
    SCREEN = pygame.display.set_mode(
        (WIDTH, HEIGHT),
        pygame.SHOWN
    )
    pygame.display.set_caption('game window')

    @staticmethod
    def update_screen(size_fullscreen=False):
        if size_fullscreen:
            WindowParams.SCREEN = pygame.display.set_mode(
                (WindowParams.SCREEN_WIDTH, WindowParams.SCREEN_HEIGHT),
                pygame.FULLSCREEN
            )
        else:
            WindowParams.SCREEN = pygame.display.set_mode(
                (WindowParams.SCREEN_WIDTH, WindowParams.SCREEN_HEIGHT)
            )


class ActionParams:
    DELAY_MAGIC_BALLS: int = 500
    LAST_MAGIC_BALLS: int = -10
    RECOVERY_MANA_BAR: int = 3000
    LAST_MANA_RECOVERED: int = -10
    FPS: int = 60
    CLOCK = pygame.time.Clock()
    TIME_ANIMATION_MAGIC_BALL: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_PORTAL: float = CLOCK.tick(FPS) / 750


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
        (1, 0, 0, 0),
        (1, 1, 0, 0),
        (0, 0, 1, 1),
        (1, 0, 1, 1),
        (1, 0, 0, 1),
        (0, 1, 1, 0)
    ]
    COUNT_ROOMS: int = len(rooms)
    NUMBER_LEVEL: int = 1
    LEVEL_ROOMS: Dict[tuple, int] = get_level(NUMBER_LEVEL)
    CURRENT_ROOM: Tuple[int, int] = (0, 0)
    GENERATED_ROOM: List[int] = [0]


class Textures:
    _loaded = False

    @classmethod
    def load_all(cls):
        if cls._loaded:
            return
        cls.WALL = pygame.image.load("textures/wall.png").convert()
        cls.FLOOR = pygame.image.load("textures/floor.png").convert()
        cls.MAGIC_BALL_BIG = pygame.image.load("textures/magicball_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL = pygame.image.load("textures/magicball_small.png").convert_alpha()
        cls.MANA_BAR_0 = pygame.image.load("textures/manabar_0.png").convert_alpha()
        cls.MANA_BAR_1 = pygame.image.load("textures/manabar_1.png").convert_alpha()
        cls.MANA_BAR_2 = pygame.image.load("textures/manabar_2.png").convert_alpha()
        cls.MANA_BAR_3 = pygame.image.load("textures/manabar_3.png").convert_alpha()
        cls.MANA_BAR_4 = pygame.image.load("textures/manabar_4.png").convert_alpha()
        cls.MANA_BAR_5 = pygame.image.load("textures/manabar_5.png").convert_alpha()
        cls.HEALTH_BAR_0 = pygame.image.load("textures/healthbar_0.png").convert_alpha()
        cls.HEALTH_BAR_1 = pygame.image.load("textures/healthbar_1.png").convert_alpha()
        cls.HEALTH_BAR_2 = pygame.image.load("textures/healthbar_2.png").convert_alpha()
        cls.HEALTH_BAR_3 = pygame.image.load("textures/healthbar_3.png").convert_alpha()
        cls.PORTAL: list = [pygame.image.load(f"textures/portals/portal_{number}.png").convert_alpha() for number in range(1, 17)]
        cls.PORTAL_STAND = pygame.image.load("textures/portal_stand.png")
        #cls.PLAYER = pygame.image.load("player.png").convert_alpha()

        cls._loaded = True
