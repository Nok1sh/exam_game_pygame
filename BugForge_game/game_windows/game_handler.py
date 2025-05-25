import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Textures
from objects.groups_objects import buttons_main_menu_group
from objects.interface_objects import ButtonMenu
from game_windows.game_window import main_game_loop, continue_from_the_save
from window_options import options_main_menu
import sys
from pathlib import Path


sys.path.append(str(Path(__file__).parent.parent))
pygame.init()

Textures.load_all()


def pass_button():
    """
    For test button
    """
    pass


def main_menu_loop() -> None:
    buttons_main_menu_group.add(
        ButtonMenu('Новая игра', 150, button_call=main_game_loop),
        ButtonMenu('Продолжить', 300, button_call=continue_from_the_save),
        ButtonMenu('Параметры', 450, button_call=options_main_menu),
        ButtonMenu('Выход', 600, button_call=pygame.quit)
    )
    while True:
        WindowParams.SCREEN.fill(Color.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for btn in buttons_main_menu_group:
                btn.type_to_button(event)

        for btn in buttons_main_menu_group:
            btn.draw(WindowParams.SCREEN)
        pygame.display.flip()


if __name__ == "__main__":
    main_menu_loop()
