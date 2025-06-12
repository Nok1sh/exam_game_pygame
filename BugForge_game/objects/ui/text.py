import pygame
from structures_and_parameters.parameters_game import Color


class TextOnWindow(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        self.x: int = x
        self.y: int = y

    def draw(self):
        pass


class TextOnWindowForGame(TextOnWindow, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        pygame.sprite.Sprite.__init__(self)
        TextOnWindow.__init__(self, x, y)
        self.size: int = 24
        self.style_text = pygame.font.SysFont('arial', self.size)

    def draw_text(self, score_money: int, screen):
        score_text = self.style_text.render(f'SCORE: {score_money}', True, Color.YELLOW)
        screen.blit(score_text, (self.x, self.y))


class TextOnWindowForOptions(TextOnWindow, pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, text: str, color: tuple, size=None):
        pygame.sprite.Sprite.__init__(self)
        TextOnWindow.__init__(self, x, y)
        self.text: str = text
        self.color: tuple = color
        self.size: int = size if size else 48
        self.style_text = pygame.font.SysFont('arial', self.size)
        self.text = self.style_text.render(self.text, True, self.color)
        self.position = self.text.get_rect(center=(self.x, self.y))

    def draw_text(self, screen) -> None:
        screen.blit(self.text, self.position)
