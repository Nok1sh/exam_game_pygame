import pygame
from structures_and_parameters.parameters_game import WindowParams, ActionParams, Textures
Textures.load_all()


class Walls(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, texture):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        tile_width, tile_height = texture.get_size()
        for tx in range(0, width, tile_width):
            for ty in range(0, height, tile_height):
                self.image.blit(texture, (tx, ty))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Doors(pygame.sprite.Sprite):
    def __init__(self, line: str, x=None, y=None):
        super().__init__()
        self.size_door: int = 2
        self.image = Textures.DOORS[line]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_door, self.image.get_height() // self.size_door))
        if line == 'vertical':
            self.rect = self.image.get_rect()
            self.rect.center = (x, WindowParams.HEIGHT//2)
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (WindowParams.WIDTH//2, y)


class Floor:
    surface = None

    @staticmethod
    def init(screen_width, screen_height):
        tile = Textures.FLOOR
        Floor.surface = pygame.Surface((screen_width, screen_height))
        for tx in range(0, screen_width, tile.get_width()):
            for ty in range(0, screen_height, tile.get_height()):
                Floor.surface.blit(tile, (tx, ty))

    @staticmethod
    def draw(screen):
        screen.blit(Floor.surface, (0, 0))


class BackgroundOptions:
    surface = None

    @staticmethod
    def init(screen_width, screen_height):
        tile = pygame.image.load(f"textures/background_options.png").convert()
        BackgroundOptions.surface = pygame.Surface((screen_width, screen_height))
        for tx in range(0, screen_width, tile.get_width()):
            for ty in range(0, screen_height, tile.get_height()):
                BackgroundOptions.surface.blit(tile, (tx, ty))

    @staticmethod
    def draw(screen):
        screen.blit(BackgroundOptions.surface, (0, 0))


class Tent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_tent: int = 5
        self.image = pygame.image.load("textures/store/tent.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_tent, self.image.get_height() // self.size_tent))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH//2, WindowParams.HEIGHT//2)


class Portal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_portal: int = 4
        self.image = pygame.image.load(f"textures/portals/portal_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_portal, self.image.get_height()//self.size_portal))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH//2, WindowParams.HEIGHT//4+100)
        self.number_portal: int = 0
        self.animation_rotation: int = 0
        self.speed_rotation: int = 8

    def update(self) -> None:
        self.animation_rotation += ActionParams.TIME_ANIMATION_PORTAL
        if self.animation_rotation >= 1.0 / self.speed_rotation:
            self.number_portal = self.number_portal % 15 + 1
            self.animation_rotation -= 1.0 / self.speed_rotation
        self.image = Textures.PORTAL[self.number_portal]
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_portal, self.image.get_height()//self.size_portal))


class PortalStand(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_portal: int = 3
        self.image = Textures.PORTAL_STAND
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_portal, self.image.get_height() // self.size_portal))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 3+100)


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.size_barrel: int = 5
        self.image = pygame.image.load("textures/barrel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_barrel, self.image.get_height() // self.size_barrel))
        self.rect = self.image.get_rect()
        self.x: int = x
        self.y: int = y
        self.rect.center = (self.x, self.y)
        self.health: int = 2


class Column(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, random_image):
        super().__init__()
        self.size_column: int = 5
        self.x: int = x
        self.y: int = y
        self.random_image = random_image
        self.image = pygame.image.load(f"textures/columns/column_{self.random_image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_column, self.image.get_height() // self.size_column))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

