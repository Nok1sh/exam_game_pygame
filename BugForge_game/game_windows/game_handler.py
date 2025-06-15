import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Textures
from objects.groups_objects import buttons_main_menu_group
from objects.ui.buttons import ButtonMenu
from game_windows.game_window import main_game_loop, continue_from_the_save
from game_windows.window_options import options_main_menu, information_menu
pygame.init()

Textures.load_all()


def pass_button():
    """
    For test button
    """
    pass


def main_menu_loop() -> None:
    buttons_main_menu_group.add(
        ButtonMenu('Новая игра', 150, button_call=main_game_loop, x=300),
        ButtonMenu('Продолжить', 300, button_call=continue_from_the_save, x=300),
        ButtonMenu('Параметры', 450, button_call=options_main_menu, x=300),
        ButtonMenu('Информация', 650, button_call=information_menu, x=WindowParams.WIDTH - 200),
        ButtonMenu('Выход', 600, button_call=pygame.quit, x=300)
    )
    background = pygame.Surface((WindowParams.WIDTH, WindowParams.HEIGHT))
    background.blit(Textures.BACKGROUND_MAIN_MENU, (0, 0))
    background.blit(Textures.TABLET_MAIN_MENU, (WindowParams.WIDTH//2+100, 0))
    while True:
        WindowParams.SCREEN.fill(Color.BLACK)
        WindowParams.SCREEN.blit(background, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for btn in buttons_main_menu_group:
                btn.type_to_button(event)

        for btn in buttons_main_menu_group:
            btn.draw(WindowParams.SCREEN)
        pygame.display.flip()

