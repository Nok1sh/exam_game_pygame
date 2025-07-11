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
    OPTION_SCREEN = pygame.display.set_mode(
        (WIDTH, HEIGHT),
    )
    icon_game = pygame.image.load("textures/hero/hero.png")
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
    DURATION_FADE_SWAP_LEVEL: int = 1500
    TIME_ANIMATION_MAGIC_BALL: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_MELEE_ENEMY: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_HERO_MOVE: float = CLOCK.tick(FPS) / 1200
    TIME_ANIMATION_COIN: float = CLOCK.tick(FPS) / 1000
    TIME_ANIMATION_PORTAL: float = CLOCK.tick(FPS) / 750
    FLAG_UPPER_HEALTH_BAR: bool = True


class Music:
    FLAG_SWAP_MUSIC: bool = True
    FLAG_RUN_MUSIC: bool = True
    BOSS_BATTLE: str = "music/boss_battle.mp3"
    BASE_BACKGROUND: str = "music/base_background2_music.mp3"
    CURRENT_MUSIC: str = BASE_BACKGROUND
    pygame.mixer.music.set_volume(0.2)

    @staticmethod
    def swap_music(trek):
        if Music.FLAG_SWAP_MUSIC and Music.FLAG_RUN_MUSIC:
            Music.CURRENT_MUSIC = trek
            pygame.mixer.fadeout(500)
            pygame.mixer.music.load(Music.CURRENT_MUSIC)
            pygame.mixer.music.play(loops=-1)

    @staticmethod
    def run_music() -> None:
        Music.FLAG_RUN_MUSIC = True
        Music.FLAG_SWAP_MUSIC = True

    @staticmethod
    def stop_music() -> None:
        pygame.mixer.music.stop()
        Music.FLAG_RUN_MUSIC = False
        Music.FLAG_SWAP_MUSIC = False


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
    _loaded: bool = False
    hero_size_width: int = 9
    hero_size_height: int = 8

    @classmethod
    def load_all(cls):
        if cls._loaded:
            return
        cls.FONT_MENU_AND_OPTIONS = pygame.font.Font("fonts/WDXLLubrifontTC-Regular.ttf", 34)
        cls.FONT_STORE = pygame.font.Font("fonts/WDXLLubrifontTC-Regular.ttf", 24)
        cls.BACKGROUND_MAIN_MENU_IMAGE = pygame.image.load("textures/main_menu_textures/background_main_menu.jpg").convert()
        cls.BACKGROUND_MAIN_MENU = pygame.transform.scale(
            cls.BACKGROUND_MAIN_MENU_IMAGE,
            (cls.BACKGROUND_MAIN_MENU_IMAGE.get_width(),
                cls.BACKGROUND_MAIN_MENU_IMAGE.get_height())
        )
        cls.TABLET_MAIN_MENU_IMAGE = pygame.image.load("textures/main_menu_textures/tablet.png").convert_alpha()
        cls.TABLET_MAIN_MENU = pygame.transform.scale(
            cls.TABLET_MAIN_MENU_IMAGE,
            (cls.TABLET_MAIN_MENU_IMAGE.get_width()//2,
             cls.TABLET_MAIN_MENU_IMAGE.get_height()//2)
        )
        cls.DOORS = {direction: pygame.image.load(f"textures/doors/door_{direction}.png").convert_alpha() for direction in ["horizontal", "vertical"]}
        cls.FLOOR = pygame.image.load(f"textures/stone_floor.png").convert()
        cls.WALL = pygame.image.load("textures/wall.png").convert()
        cls.BUTTON_MENU_AND_OPTIONS_NORMAL = pygame.image.load(f"textures/buttons/button_menu.png").convert_alpha()
        cls.BUTTON_MENU_AND_OPTIONS_HOVER = pygame.image.load(f"textures/buttons/button_menu_hover.png").convert_alpha()
        cls.BUTTON_STORE_NORMAL = pygame.image.load(f"textures/buttons/button_store.png").convert_alpha()
        cls.BUTTON_STORE_HOVER = pygame.image.load(f"textures/buttons/button_store_hover.png").convert_alpha()
        cls.MAGIC_BALL_BIG = pygame.image.load("textures/magicballs/magicball_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL = pygame.image.load("textures/magicballs/magicball_small.png").convert_alpha()
        cls.MAGIC_BALL_BIG_ENEMY = pygame.image.load("textures/magicballs/magicball_enemy_big.png").convert_alpha()
        cls.MAGIC_BALL_SMALL_ENEMY = pygame.image.load("textures/magicballs/magicball_enemy_small.png").convert_alpha()
        cls.MANA_BARS = [pygame.image.load(f"textures/manabar/manabar_{number}.png").convert_alpha() for number in range(6)]
        cls.HEALTH_BARS = [pygame.image.load(f"textures/healthbar/healthbar_{number}.png").convert_alpha() for number in range(4)]
        cls.HEALTH_BARS_BIG = [pygame.image.load(f"textures/healthbar2/healthbar_{number}.png").convert_alpha() for number in range(5)]
        cls.MONEY_BAR = pygame.image.load("textures/money_bar.png").convert_alpha()
        cls.PORTAL: list = [pygame.image.load(f"textures/portals/portal_{number}.png").convert_alpha() for number in range(1, 17)]
        cls.PORTAL_STAND = pygame.image.load("textures/portals/portal_stand.png").convert_alpha()
        cls.COIN = [pygame.image.load(f"textures/coin/money_{number}.png").convert_alpha() for number in range(1, 7)]
        cls.COLUMN = [pygame.image.load(f"textures/columns/column_{number}.png").convert_alpha() for number in range(1, 7)]
        cls.MELEE_ENEMY = [pygame.image.load(f"textures/melee_enemy/melee_enemy_{number}.png").convert_alpha() for number in range(1, 6)]
        cls.RANGE_ENEMY = [pygame.image.load(f"textures/range_enemy/range_enemy_{number}.png").convert_alpha() for number in range(1, 27)]
        cls.BOSS_RANGE_ENEMY = [pygame.image.load(f"textures/boss_range_enemy/boss_range_enemy{number}.png").convert_alpha() for number in range(1, 25)]
        cls.PLAYER = [pygame.image.load(f"textures/hero/hero_move{number}.png").convert_alpha() for number in range(1, 17)]
        cls.PLAYER_HORIZONTAL = {number: pygame.transform.scale(cls.PLAYER[number-1],
                                                                (cls.PLAYER[number-1].get_width()//cls.hero_size_height,
                                                                 cls.PLAYER[number-1].get_height()//cls.hero_size_width)).convert_alpha() for number in [5, 6, 15, 16]}
        cls.PLAYER_VERTICAL = {number: pygame.transform.scale(cls.PLAYER[number - 1],
                                                                (cls.PLAYER[number - 1].get_width() // cls.hero_size_width,
                                                                 cls.PLAYER[number - 1].get_height() // cls.hero_size_height)).convert_alpha() for number in [1, 2, 7, 8]}
        cls.PLAYER_DIAGONAL = {number: pygame.transform.scale(cls.PLAYER[number - 1],
                                                              (cls.PLAYER[number - 1].get_width() // cls.hero_size_width,
                                                              cls.PLAYER[number - 1].get_height() // cls.hero_size_width)).convert_alpha() for number in [3, 4, 9, 10, 11, 12, 13, 14]}

        cls._loaded = True
