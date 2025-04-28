import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Textures, Rooms, ActionParams
from objects.groups_objects import buttons_main_menu_group
from objects.interface_objects import ButtonMainMenu
from game_windows.game_window import main_game_loop
from window_options import options_main_menu
import importlib
import structures_and_parameters.parameters_game
pygame.init()

Textures.load_all()


def main_menu_loop():
    buttons_main_menu_group.add(
        ButtonMainMenu('Новая игра', 200, button_call=main_game_loop),
        ButtonMainMenu('Параметры', 350, button_call=options_main_menu),
        ButtonMainMenu('Выход', 500, button_call=pygame.quit)
    )
    while True:
        #importlib.reload()
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
