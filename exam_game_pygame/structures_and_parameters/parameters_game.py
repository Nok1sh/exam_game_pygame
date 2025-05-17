import pygame
from typing import Tuple
pygame.init()


class WindowParams:
    info = pygame.display.Info()
    WIDTH: int = int(info.current_w*0.8)
    HEIGHT: int = int(info.current_h*0.8)
    SCREEN_WIDTH: int = WIDTH
    SCREEN_HEIGHT: int = HEIGHT
    FLAG_RETURN_TO_MAIN_MENU: bool = False
    SCREEN = pygame.display.set_mode(
        (WIDTH, HEIGHT),
        pygame.SHOWN
    )
    pygame.display.set_caption('game window')

    @staticmethod
    def update_screen(size_fullscreen=False) -> None:
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
    TIME_ANIMATION_HERO_MOVE: float = CLOCK.tick(FPS) / 5000
    TIME_ANIMATION_COIN: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_PORTAL: float = CLOCK.tick(FPS) / 750


class Color:
    WHITE: Tuple[int, int, int] = (255, 255, 255)
    RED: Tuple[int, int, int] = (255, 0, 0)
    GREEN: Tuple[int, int, int] = (0, 255, 0)
    DARK_GREEN: Tuple[int, int, int] = (0, 100, 0)
    BLUE: Tuple[int, int, int] = (0, 0, 255)
    BLACK: Tuple[int, int, int] = (0, 0, 0)
    YELLOW: Tuple[int, int, int] = (255, 255, 0)
    DARKER_YELLOW: Tuple[int, int, int] = (200, 200, 0)
    VIOLET: Tuple[int, int, int] = (128, 0, 128)
    ORANGE: Tuple[int, int, int] = (255, 165, 0)
    PINK: Tuple[int, int, int] = (255, 192, 203)
    GRAY: Tuple[int, int, int] = (128, 128, 128)
    TURQUOISE: Tuple[int, int, int] = (64, 224, 208)


class Textures:
    _loaded = False

    @classmethod
    def load_all(cls):
        if cls._loaded:
            return
        cls.WALL = pygame.image.load("../exam_game_pygame/textures/wall.png").convert()
        cls.FLOOR = pygame.image.load("../exam_game_pygame/textures/floor.png").convert()
        cls.MAGIC_BALL_BIG = pygame.image.load("../exam_game_pygame/textures/magicball_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL = pygame.image.load("../exam_game_pygame/textures/magicball_small.png").convert_alpha()
        cls.MAGIC_BALL_BIG_ENEMY = pygame.image.load("../exam_game_pygame/textures/magicball_enemy_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL_ENEMY = pygame.image.load("../exam_game_pygame/textures/magicball_enemy_small.png").convert_alpha()
        cls.MANA_BAR_0 = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_0.png").convert_alpha()
        cls.MANA_BAR_1 = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_1.png").convert_alpha()
        cls.MANA_BAR_2 = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_2.png").convert_alpha()
        cls.MANA_BAR_3 = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_3.png").convert_alpha()
        cls.MANA_BAR_4 = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_4.png").convert_alpha()
        cls.MANA_BAR_5 = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_5.png").convert_alpha()
        cls.HEALTH_BAR_0 = pygame.image.load("../exam_game_pygame/textures/healthbar/healthbar_0.png").convert_alpha()
        cls.HEALTH_BAR_1 = pygame.image.load("../exam_game_pygame/textures/healthbar/healthbar_1.png").convert_alpha()
        cls.HEALTH_BAR_2 = pygame.image.load("../exam_game_pygame/textures/healthbar/healthbar_2.png").convert_alpha()
        cls.HEALTH_BAR_3 = pygame.image.load("../exam_game_pygame/textures/healthbar/healthbar_3.png").convert_alpha()
        cls.MONEY_BAR = pygame.image.load("../exam_game_pygame/textures/money_bar.png").convert_alpha()
        cls.PORTAL: list = [pygame.image.load(f"../exam_game_pygame/textures/portals/portal_{number}.png").convert_alpha() for number in range(1, 17)]
        cls.PORTAL_STAND = pygame.image.load("../exam_game_pygame/textures/portal_stand.png")
        cls.COIN = [pygame.image.load(f"../exam_game_pygame/textures/coin/money_{number}.png").convert_alpha() for number in range(1, 7)]
        cls.COLUMN = [pygame.image.load(f"../exam_game_pygame/textures/columns/column_{number}.png").convert_alpha() for number in range(1, 7)]
        #cls.PLAYER = pygame.image.load("player.png").convert_alpha()

        cls._loaded = True
