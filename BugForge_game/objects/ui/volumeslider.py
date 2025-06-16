import pygame
from structures_and_parameters.parameters_game import Textures, Color, WindowParams


class VolumeSlider:
    def __init__(self, x: int = WindowParams.WIDTH//2, y: int = WindowParams.HEIGHT//2+200):
        self.x: int = x
        self.y: int = y
        self.width: int = 600
        self.height: int = 20
        self.bar_rect = pygame.Rect(self.x-self.width//2, self.y, self.width, self.height)
        self.handle_rect = pygame.Rect(self.x, self.y - 5, 10, 30)
        self.dragging = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.dragging = False
        elif event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x = event.pos[0]
            new_x = max(self.bar_rect.left, min(mouse_x, self.bar_rect.right))
            self.handle_rect.centerx = new_x
            self.update_volume()

    def update_volume(self):
        percent = (self.handle_rect.centerx - self.bar_rect.left) / self.bar_rect.width
        pygame.mixer.music.set_volume(percent)

    def draw(self, surface):
        pygame.draw.rect(surface, Color.GRAY, self.bar_rect)
        pygame.draw.rect(surface, Color.DARKER_YELLOW, self.handle_rect)

        font = Textures.FONT_MENU_AND_OPTIONS
        volume = pygame.mixer.music.get_volume()
        vol_text = font.render(f"Громкость: {int(volume * 100)}%", True, Color.WHITE)
        surface.blit(vol_text, (self.bar_rect.x, self.bar_rect.y - 60))
