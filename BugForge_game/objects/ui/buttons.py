import pygame
from structures_and_parameters.parameters_game import WindowParams, Color


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
