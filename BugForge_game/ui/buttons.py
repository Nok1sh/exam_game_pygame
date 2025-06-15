import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Textures


class Button(pygame.sprite.Sprite):
    def __init__(self, text: str, y: int, x=None, button_call=None, width=None, height=None):
        super().__init__()
        self.text: str = text
        self.width: int = width if width else 400
        self.height: int = height if height else 100
        self.call = button_call
        self.hovered: bool = False
        self.FONT = Textures.FONT_MENU_AND_OPTIONS
        self.image_normal = Textures.BUTTON_MENU_AND_OPTIONS_NORMAL
        self.image_normal = pygame.transform.scale(self.image_normal, (self.width, self.height))
        self.image_hover = Textures.BUTTON_MENU_AND_OPTIONS_HOVER
        self.image_hover = pygame.transform.scale(self.image_hover, (self.width, self.height))
        self.image = self.image_normal
        self.rect = self.image.get_rect()

    def draw(self, surface) -> None:
        self.image = self.image_hover if self.hovered else self.image_normal
        surface.blit(self.image, self.rect)
        text_surf = self.FONT.render(self.text, True, Color.WHITE)
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
        self.height: int = 100
        self.width: int = 410
        self.x: int = x if x else WindowParams.WIDTH//2
        self.rect.center = (self.x, y)
        self.image_normal = Textures.BUTTON_STORE_NORMAL
        self.image_hover = Textures.BUTTON_STORE_HOVER
        self.image_normal = pygame.transform.scale(self.image_normal, (self.width, self.height))
        self.image_hover = pygame.transform.scale(self.image_hover, (self.width, self.height))
        self.FONT = Textures.FONT_STORE

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

