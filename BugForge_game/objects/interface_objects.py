import pygame
from structures_and_parameters.parameters_game import WindowParams, ActionParams, Textures, Color
import math
import random


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
    def __init__(self, line: str, x=None, y=None):
        super().__init__()
        self.size_door: int = 2
        self.image = pygame.image.load(f"../exam_game_pygame/textures/door_{line}.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_door, self.image.get_height() // self.size_door))
        if line == 'vertical':
            self.rect = self.image.get_rect()
            self.rect.center = (x, WindowParams.HEIGHT//2)
        else:
            self.rect = self.image.get_rect()
            self.rect.center = (WindowParams.WIDTH//2, y)


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
        self.image = pygame.image.load("../exam_game_pygame/textures/manabar/manabar_5.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size_width, self.image.get_height()//self.size_height))
        self.rect = self.image.get_rect()
        self.rect.x = 10
        self.rect.y = WindowParams.HEIGHT-45

    def __recovery_mana_bar(self) -> None:
        if self.player.mana_pool != 5:
            if pygame.time.get_ticks() - ActionParams.LAST_MANA_RECOVERED >= ActionParams.RECOVERY_MANA_BAR:
                self.player.mana_pool += 1
                ActionParams.LAST_MANA_RECOVERED = pygame.time.get_ticks()

    def update(self) -> None:
        mana_bar_textures: list = Textures.MANA_BARS
        self.image = mana_bar_textures[self.player.mana_pool]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.__recovery_mana_bar()


class HealthBar(pygame.sprite.Sprite):

    FLAG_SWAP: bool = False

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.size_width: int = 2
        self.size_height: int = 3
        self.image = pygame.image.load("../exam_game_pygame/textures/healthbar2/healthbar_4.png").convert_alpha() \
            if ActionParams.FLAG_UPPER_HEALTH_BAR \
            else pygame.image.load("../exam_game_pygame/textures/healthbar/healthbar_3.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect()
        self.rect.y = WindowParams.HEIGHT - 45
        self.rect.right = WindowParams.WIDTH - (8 if ActionParams.FLAG_UPPER_HEALTH_BAR else -52)

    def update(self) -> None:
        if HealthBar.FLAG_SWAP:
            HealthBar.FLAG_SWAP = False
            self.rect.y = WindowParams.HEIGHT - 45
            self.rect.right = WindowParams.WIDTH - (8 if ActionParams.FLAG_UPPER_HEALTH_BAR else -52)
        health_bar_textures: list = Textures.HEALTH_BARS_BIG if ActionParams.FLAG_UPPER_HEALTH_BAR \
            else Textures.HEALTH_BARS
        self.image = health_bar_textures[math.ceil(self.player.health_bar)]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))


class MoneyBar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_width: int = 1
        self.size_height: int = 2
        self.image = pygame.image.load("../exam_game_pygame/textures/money_bar.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect()
        self.rect.center = (135, 22)


class Tent(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_tent: int = 5
        self.image = pygame.image.load("../exam_game_pygame/textures/store/tent.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_tent, self.image.get_height() // self.size_tent))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH//2, WindowParams.HEIGHT//2)


class Trader(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size: int = 1
        self.image = pygame.image.load("../exam_game_pygame/textures/store/steampunk_trader.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size, self.image.get_height() // self.size))
        self.rect = self.image.get_rect()
        self.rect.center = ((WindowParams.WIDTH//4)*3-50, WindowParams.HEIGHT//2+100)


class StoreMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("../exam_game_pygame/textures/store/store_menu.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                                (self.image.get_width() * 1.5, self.image.get_height() // 1))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2)


class Portal(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_portal: int = 4
        self.image = pygame.image.load(f"../exam_game_pygame/textures/portals/portal_1.png").convert_alpha()
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
        self.image = pygame.image.load("../exam_game_pygame/textures/portal_stand.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_portal, self.image.get_height() // self.size_portal))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 3+100)


class Barrel(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.size_barrel: int = 5
        self.image = pygame.image.load("../exam_game_pygame/textures/barrel.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_barrel, self.image.get_height() // self.size_barrel))
        self.rect = self.image.get_rect()
        self.x: int = x
        self.y: int = y
        self.rect.center = (self.x, self.y)
        self.health: int = 2

    def update(self, magic_balls, projectiles, player, moneys_group, potions) -> None:
        collision_enemy_magic_balls = pygame.sprite.spritecollide(self, projectiles, True)
        collision_magic_balls = pygame.sprite.spritecollide(self, magic_balls, True)
        if collision_magic_balls or collision_enemy_magic_balls:
            self.health -= 1
            if self.health <= 0:
                self.kill()
                chance_drop: float = random.random()
                if chance_drop <= 0.2:
                    moneys_group.add(Coin(self.x, self.y))
                elif chance_drop <= 0.4:
                    potions.add(Potion(self.x, self.y, "health"))
                elif chance_drop <= 0.7:
                    potions.add(Potion(self.x, self.y, "mana"))


class Column(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, random_image):
        super().__init__()
        self.size_column: int = 5
        self.x: int = x
        self.y: int = y
        self.random_image = random_image
        self.image = pygame.image.load(f"../exam_game_pygame/textures/columns/column_{self.random_image}.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_column, self.image.get_height() // self.size_column))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

    def update(self, magic_balls) -> None:
        pygame.sprite.spritecollide(self, magic_balls, True)


class Coin(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.size: int = 3
        self.score: int = 50
        self.image = pygame.image.load("../exam_game_pygame/textures/coin/money_1.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width()//self.size, self.image.get_height()//self.size))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.speed_rotation: int = 7
        self.animation_money: int = 0
        self.number_image: int = 1

    def update(self) -> None:
        self.animation_money += ActionParams.TIME_ANIMATION_COIN
        if self.animation_money >= 1.0 / self.speed_rotation:
            self.number_image = self.number_image % 6 + 1
            self.animation_money -= 1.0 / self.speed_rotation
        self.image = Textures.COIN[self.number_image-1]
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size, self.image.get_height() // self.size))


class Potion(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.name: str = name
        self.size_potion: int = 20
        self.image = pygame.image.load(f"../exam_game_pygame/textures/potions/{name}_potion.png")
        self.image = pygame.transform.scale(self.image,(self.image.get_width() // self.size_potion, self.image.get_height() // self.size_potion))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)


class Button(pygame.sprite.Sprite):
    def __init__(self, text: str, y: int, x=None, button_call=None, width=None, height=None):
        super().__init__()
        self.text: str = text
        self.width: int = width if width else 400
        self.height: int = height if height else 100
        self.image = pygame.Surface([self.width, self.height])
        self.rect = self.image.get_rect()
        self.call = button_call
        self.hovered: bool = False
        self.FONT = pygame.font.SysFont("arial", 50)
        self.SMALL_FONT = pygame.font.SysFont("arial", 32)

    def draw(self, surface) -> None:
        color = Color.BLUE if self.hovered else Color.GRAY
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surf = self.SMALL_FONT.render(self.text, True, Color.WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def type_to_button(self, event) -> None:
        pass


class ButtonMenu(Button, pygame.sprite.Sprite):
    def __init__(self, text: str, y: int, button_call, x=None, width=None, height=None):
        pygame.sprite.Sprite.__init__(self)
        Button.__init__(self, text=text, y=y, button_call=button_call, width=width, height=height)
        self.x: int = x if x else WindowParams.WIDTH//2
        self.rect.center = (self.x, y)

    def type_to_button(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.call()


class ButtonAction(Button, pygame.sprite.Sprite):
    def __init__(self, text: str, y: int, button_call, x=None):
        pygame.sprite.Sprite.__init__(self)
        Button.__init__(self, text=text, y=y, button_call=button_call)
        self.height: int = 60
        self.width: int = 500
        self.x: int = x if x else WindowParams.WIDTH//2
        self.rect.center = (self.x, y)
        self.FONT = pygame.font.SysFont("arial", 42)
        self.SMALL_FONT = pygame.font.SysFont("arial", 24)

    def draw(self, surface) -> None:
        color = Color.DARKER_YELLOW if self.hovered else Color.GRAY
        pygame.draw.rect(surface, color, self.rect, border_radius=10)
        text_surf = self.SMALL_FONT.render(self.text, True, Color.WHITE)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def type_to_button(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.call()


class ButtonBack(Button, pygame.sprite.Sprite):
    def __init__(self, text: str, y: int, x: int):
        pygame.sprite.Sprite.__init__(self)
        Button.__init__(self, text=text, y=y)
        self.flag_back: bool = False
        self.rect.center = (x, y)

    def type_to_button(self, event) -> None:
        if event.type == pygame.MOUSEMOTION:
            self.hovered = self.rect.collidepoint(event.pos)
        elif event.type == pygame.MOUSEBUTTONDOWN and self.hovered:
            self.flag_back = True


class TextOnWindowForGame(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x: int = x
        self.y: int = y

    def draw_score_money(self, score_money: int, screen):
        style_text = pygame.font.SysFont('arial', 24)
        score_text = style_text.render(f'SCORE: {score_money}', 1, Color.YELLOW)
        screen.blit(score_text, (self.x, self.y))


class TextOnWindowForOptions(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, text: str, color: tuple, size=None):
        super().__init__()
        self.x: int = x
        self.y: int = y
        self.text: str = text
        self.color: tuple = color
        self.size: int = size if size else 48

    def draw_text(self, screen) -> None:
        style_text = pygame.font.SysFont('arial', self.size)
        text = style_text.render(self.text, True, self.color)
        position = text.get_rect(center=(self.x, self.y))
        screen.blit(text, position)


