import pygame
from parameters_game import WindowParams, ActionParams, Textures, Color
import math


class Walls(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int, texture):
        super().__init__()
        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        tile_width, tile_height = texture.get_size()
        for tx in range(0, width, tile_width):
            for ty in range(0, height, tile_height):
                self.image.blit(texture, (tx, ty))
        # self.image.fill(Color.DARK_GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Doors(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, width: int, height: int):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(Color.BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Floor:
    @staticmethod
    def floor(screen):
        tile_width, tile_height = Textures.FLOOR.get_size()
        for tx in range(0, WindowParams.WIDTH, tile_width):
            for ty in range(0, WindowParams.HEIGHT, tile_height):
                screen.blit(Textures.FLOOR, (tx, ty))


class ManaBar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.size_width: int = 2
        self.size_height: int = 3
        self.image = pygame.image.load("textures/manabar_5.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_width, self.image.get_height()//self.size_height))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = WindowParams.HEIGHT-45

    def __recovery_mana_bar(self):
        if self.player.mana_pool != 5:
            if pygame.time.get_ticks() - ActionParams.LAST_MANA_RECOVERED >= ActionParams.RECOVERY_MANA_BAR:
                self.player.mana_pool += 1
                ActionParams.LAST_MANA_RECOVERED = pygame.time.get_ticks()

    def update(self):
        mana_bar_textures: list = [Textures.MANA_BAR_0, Textures.MANA_BAR_1, Textures.MANA_BAR_2, Textures.MANA_BAR_3, Textures.MANA_BAR_4, Textures.MANA_BAR_5]
        self.image = mana_bar_textures[self.player.mana_pool]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.__recovery_mana_bar()


class HealthBar(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.size_width: int = 2
        self.size_height: int = 3
        self.image = pygame.image.load("textures/healthbar_3.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect()
        self.rect.x = WindowParams.WIDTH - 230
        self.rect.y = WindowParams.HEIGHT - 45

    def update(self):
        health_bar_textures: list = [Textures.HEALTH_BAR_0, Textures.HEALTH_BAR_1, Textures.HEALTH_BAR_2, Textures.HEALTH_BAR_3]
        self.image = health_bar_textures[math.ceil(self.player.health_bar)]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        #self.__recovery_mana_bar()


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

    def update(self):
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
        self.image = pygame.image.load("textures/portal_stand.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_portal, self.image.get_height() // self.size_portal))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 3+100)


class ButtonMainMenu(pygame.sprite.Sprite):
    def __init__(self, text: str, y: int, button_call):
        super().__init__()
        self.text: str = text
        self.width: int = 400
        self.height: int = 100
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH//2, y)
        self.call = button_call
        self.hovered: bool = False
        self.FONT = pygame.font.SysFont("arial", 50)
        self.SMALL_FONT = pygame.font.SysFont("arial", 32)

    def draw(self, surface):
        color = Color.BLUE if self.hovered else Color.GRAY
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surf = self.SMALL_FONT.render(self.text, True, Color.WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def type_to_button(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.call()


class ButtonBack(pygame.sprite.Sprite):
    def __init__(self, text: str, x: int, y: int):
        super().__init__()
        self.flag_back: bool = False
        self.hovered: bool = False
        self.text: str = text
        self.x: int = x
        self.y: int = y
        self.width: int = 400
        self.height: int = 100
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.FONT = pygame.font.SysFont("arial", 50)
        self.SMALL_FONT = pygame.font.SysFont("arial", 32)

    def draw(self, surface):
        color = Color.BLUE if self.hovered else Color.GRAY
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surf = self.SMALL_FONT.render(self.text, True, Color.WHITE)
        position = text_surf.get_rect(center=(self.x, self.y))
        surface.blit(text_surf, position)

    def type_to_button(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.flag_back = True


class TextOnWindow(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, text: str, color: tuple):
        super().__init__()
        self.x: int = x
        self.y: int = y
        self.text: str = text
        self.color: tuple = color

    def draw_text(self, screen):
        style_text = pygame.font.SysFont('arial', 48)
        text = style_text.render(self.text, 1, self.color)
        position = text.get_rect(center=(self.x, self.y))
        screen.blit(text, position)


