import pygame
from typing import Dict
from structures_and_parameters.parameters_game import WindowParams, Textures, ActionParams


class PlayerRender(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.size_width: int = 9
        self.size_height: int = 8
        self.image = pygame.image.load("textures/hero/hero.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, (
        self.image.get_width() // self.size_width, self.image.get_height() // self.size_height))
        self.rect = self.image.get_rect()
        self.rect.center = (WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2)
        self.animation_lines: Dict[str, int] = {
            "top": 1, "right_top": 3, "right": 5, "bottom": 7, "left_top": 9,
            "right_bottom": 11, "left_bottom": 13, "left": 15
        }
        self.animation_moves: Dict[str, int] = {
            "top": 0, "right_top": 0, "right": 0, "bottom": 0, "left_top": 0,
            "right_bottom": 0, "left_bottom": 0, "left": 0
        }
        self.animation_lines_constant: Dict[str, tuple] = {
            "top": (1, 2), "right_top": (3, 4), "right": (5, 6), "bottom": (7, 8), "left_top": (9, 10),
            "right_bottom": (11, 12), "left_bottom": (13, 14), "left": (15, 16)
        }
        self.speed_animation: int = 10
        self.animation_move: int = 0

    def update(self, player):
        self.rect.topleft = (player.rect.x, player.rect.y)
        if player.flag_swap_image:
            self.__animation_move_hero(player.line_move, player.direction_move, player)

    def __swap_image(self, number: int, line: str, player) -> None:
        """
        Changing the image of the hero when moving
        """
        self.image = Textures.PLAYER[number-1]
        if line == "horizontal":
            self.image = Textures.PLAYER_HORIZONTAL[number]
        elif line == "vertical":
            self.image = Textures.PLAYER_VERTICAL[number]
        else:
            self.image = Textures.PLAYER_DIAGONAL[number]
        player.flag_swap_image = False

    def __animation_move_hero(self, line: str, direction: str, player) -> None:
        """
        Handling hero animation when moving
        """
        self.animation_moves[line] += ActionParams.TIME_ANIMATION_HERO_MOVE
        if self.animation_moves[line] >= 1 / self.speed_animation:
            self.animation_moves[line] -= 1.0 / self.speed_animation
            self.__swap_image(self.animation_lines[line], direction, player)
            self.animation_lines[line] = self.animation_lines_constant[line][1] \
                if self.animation_lines[line] == self.animation_lines_constant[line][0] \
                else self.animation_lines_constant[line][0]