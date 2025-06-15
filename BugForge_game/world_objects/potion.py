import pygame


class Potion(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, name: str):
        super().__init__()
        self.name: str = name
        self.size_potion: int = 20
        self.image = pygame.image.load(f"textures/potions/{name}_potion.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() // self.size_potion, self.image.get_height() // self.size_potion))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
