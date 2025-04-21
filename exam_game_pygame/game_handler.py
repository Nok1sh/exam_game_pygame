import pygame
from parameters_game import WindowParams, Color, Textures
from groups_objects import buttons_main_menu_group, ButtonMainMenu
from game_window import main_game_loop
from window_options import options
pygame.init()

Textures.load_all()


def main_menu_loop():
    buttons_main_menu_group.add(
        ButtonMainMenu('Новая игра', 200, main_game_loop),
        ButtonMainMenu('Параметры', 350, options),
        ButtonMainMenu('Выход', 500, pygame.quit)
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
