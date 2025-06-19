import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Music
from objects.ui.text import TextOnWindowForOptions
from objects.ui.buttons import ButtonMenu, ButtonBack
from objects.ui.volumeslider import VolumeSlider
from objects.world_objects.background_options import BackgroundOptions


def parameters_in_game() -> None:
    """
    Window with changing game parameters
    """
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu(f'Включить музыку', WindowParams.HEIGHT // 2 - 100, x=WindowParams.WIDTH // 2 - 180,
                   button_call=Music.run_music, width=300, height=75),
        ButtonMenu(f'Выключить музыку', WindowParams.HEIGHT // 2 - 100, x=WindowParams.WIDTH // 2 + 180,
                   button_call=Music.stop_music, width=300, height=75)
    )
    button_back_group = pygame.sprite.Group(
        ButtonBack('Назад', WindowParams.HEIGHT // 2 + 325, 200)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 200, 'Игровые параметры ', Color.WHITE)
    )
    volume_slider = VolumeSlider(y=WindowParams.HEIGHT//2+100)
    while True:
        BackgroundOptions.draw(WindowParams.OPTION_SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            volume_slider.handle_event(event)

            for btn in buttons_options_group:
                btn.type_to_button(event)
            for back in button_back_group:
                back.type_to_button(event)
                if back.flag_back:
                    return

        volume_slider.draw(WindowParams.OPTION_SCREEN)

        for btn in text_options_group:
            btn.draw_text(WindowParams.OPTION_SCREEN)
        for btn in buttons_options_group:
            btn.draw(WindowParams.OPTION_SCREEN)
        for btn in button_back_group:
            btn.draw(WindowParams.OPTION_SCREEN)
        pygame.display.flip()


def options_in_game() -> None:
    """
    Pause window
    """
    continue_game: bool = False
    back_to_main_menu: bool = False

    def continue_game_button() -> None:
        nonlocal continue_game
        continue_game = True

    def return_to_main_menu() -> None:
        nonlocal back_to_main_menu
        back_to_main_menu = True
        WindowParams.FLAG_RETURN_TO_MAIN_MENU = True

    continue_game = False
    back_to_main_menu = False
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu('Продолжить', WindowParams.HEIGHT // 2 - 200, continue_game_button),
        ButtonMenu('Вернуться в главное меню', WindowParams.HEIGHT // 2 - 50, return_to_main_menu),
        ButtonMenu('Параметры', WindowParams.HEIGHT // 2 + 100, parameters_in_game),
        ButtonMenu(f'Выйти из игры', WindowParams.HEIGHT // 2 + 250, pygame.quit)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 300, 'Настройки', Color.WHITE)
    )
    while True:
        BackgroundOptions.draw(WindowParams.OPTION_SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for btn in buttons_options_group:
                btn.type_to_button(event)
                if continue_game:
                    return
                if back_to_main_menu:
                    return
        for btn in text_options_group:
            btn.draw_text(WindowParams.OPTION_SCREEN)
        for btn in buttons_options_group:
            btn.draw(WindowParams.OPTION_SCREEN)
        pygame.display.flip()

