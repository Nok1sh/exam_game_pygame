import pygame
from typing import Tuple
pygame.init()


class WindowParams:
    """
    Game window settings
    """
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
    icon_game = pygame.image.load("../textures/hero/hero.png")
    pygame.display.set_icon(icon_game)
    pygame.display.set_caption("Bugforge")

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
    """
    Parameters of active constants and animations
    """
    DELAY_MAGIC_BALLS: int = 500
    LAST_MAGIC_BALLS: int = -10
    RECOVERY_MANA_BAR: int = 3000
    LAST_MANA_RECOVERED: int = -10
    FPS: int = 60
    CLOCK = pygame.time.Clock()
    TIME_ANIMATION_MAGIC_BALL: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_MELEE_ENEMY: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_HERO_MOVE: float = CLOCK.tick(FPS) / 3000
    TIME_ANIMATION_COIN: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_PORTAL: float = CLOCK.tick(FPS) / 750
    FLAG_UPPER_HEALTH_BAR: bool = True


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
        cls.WALL = pygame.image.load("../textures/wall.png").convert()
        #cls.FLOOR = pygame.image.load("../textures/floor.png").convert()
        cls.MAGIC_BALL_BIG = pygame.image.load("../textures/magicballs/magicball_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL = pygame.image.load("../textures/magicballs/magicball_small.png").convert_alpha()
        cls.MAGIC_BALL_BIG_ENEMY = pygame.image.load("../textures/magicballs/magicball_enemy_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL_ENEMY = pygame.image.load("../textures/magicballs/magicball_enemy_small.png").convert_alpha()
        cls.MANA_BARS = [pygame.image.load(f"../textures/manabar/manabar_{number}.png").convert_alpha() for number in range(6)]
        cls.HEALTH_BARS = [pygame.image.load(f"../textures/healthbar/healthbar_{number}.png").convert_alpha() for number in range(4)]
        cls.HEALTH_BARS_BIG = [pygame.image.load(f"../textures/healthbar2/healthbar_{number}.png").convert_alpha() for number in range(5)]
        cls.MONEY_BAR = pygame.image.load("../textures/money_bar.png").convert_alpha()
        cls.PORTAL: list = [pygame.image.load(f"../textures/portals/portal_{number}.png").convert_alpha() for number in range(1, 17)]
        cls.PORTAL_STAND = pygame.image.load("../textures/portal_stand.png")
        cls.COIN = [pygame.image.load(f"../textures/coin/money_{number}.png").convert_alpha() for number in range(1, 7)]
        cls.COLUMN = [pygame.image.load(f"../textures/columns/column_{number}.png").convert_alpha() for number in range(1, 7)]
        cls.MELEE_ENEMY = [pygame.image.load(f"../textures/melee_enemy/melee_enemy_{number}.png").convert_alpha() for number in range(1, 6)]
        cls.RANGE_ENEMY = [pygame.image.load(f"../textures/range_enemy/range_enemy_{number}.png").convert_alpha() for number in range(1, 27)]
        #cls.PLAYER = pygame.image.load("player.png").convert_alpha()
        cls.FLOOR = pygame.image.load(f"../textures/stone_floor.png")

        cls._loaded = True
