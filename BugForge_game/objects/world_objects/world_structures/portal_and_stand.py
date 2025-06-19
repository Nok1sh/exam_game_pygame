import pygame
from structures_and_parameters.parameters_game import WindowParams, ActionParams, Textures
Textures.load_all()


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
