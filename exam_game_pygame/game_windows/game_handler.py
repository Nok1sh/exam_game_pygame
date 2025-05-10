import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Textures
from objects.groups_objects import buttons_main_menu_group
from objects.interface_objects import ButtonMenu
from game_windows.game_window import main_game_loop
from window_options import options_main_menu
pygame.init()

Textures.load_all()


def main_menu_loop() -> None:
    buttons_main_menu_group.add(
        ButtonMenu('Новая игра', 200, button_call=main_game_loop),
        ButtonMenu('Параметры', 350, button_call=options_main_menu),
        ButtonMenu('Выход', 500, button_call=pygame.quit)
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
