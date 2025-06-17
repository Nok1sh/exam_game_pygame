import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, ActionParams, Music
from objects.ui.bars import HealthBar
from objects.ui.text import TextOnWindowForOptions
from objects.ui.buttons import ButtonMenu, ButtonBack
from objects.ui.volumeslider import VolumeSlider
from objects.world_objects.world_structures import BackgroundOptions


BackgroundOptions.init(WindowParams.WIDTH, WindowParams.HEIGHT)


def fullscreen() -> None:
    WindowParams.update_screen(size_fullscreen=True)


def window_screen() -> None:
    WindowParams.update_screen()


def change_health_bar_big() -> None:
    ActionParams.FLAG_UPPER_HEALTH_BAR = True
    HealthBar.FLAG_SWAP = True


def change_health_bar_small() -> None:
    ActionParams.FLAG_UPPER_HEALTH_BAR = False
    HealthBar.FLAG_SWAP = True


def options_main_menu() -> None:
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu('Полный экран', WindowParams.HEIGHT // 2 - 200, x=WindowParams.WIDTH//2 - 180, button_call=fullscreen, width=300, height=75),
            ButtonMenu(f'Оконный режим', WindowParams.HEIGHT // 2 - 200, x=WindowParams.WIDTH//2 + 180, button_call=window_screen, width=300, height=75),
            ButtonMenu(f'Увеличенное здоровье', WindowParams.HEIGHT // 2, x=WindowParams.WIDTH//2 - 180, button_call=change_health_bar_big, width=300, height=75),
            ButtonMenu(f'Уменьшенное здоровье', WindowParams.HEIGHT // 2, x=WindowParams.WIDTH//2 + 180, button_call=change_health_bar_small, width=300, height=75),
            ButtonMenu(f'Включить музыку', WindowParams.HEIGHT // 2 + 100, x=WindowParams.WIDTH // 2 - 180, button_call=Music.run_music, width=300, height=75),
            ButtonMenu(f'Выключить музыку', WindowParams.HEIGHT // 2 + 100, x=WindowParams.WIDTH // 2 + 180, button_call=Music.stop_music, width=300, height=75)
    )
    button_back_group = pygame.sprite.Group(
        ButtonBack('Назад', WindowParams.HEIGHT // 2 + 325, 200)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 300, 'Расширение', Color.WHITE),
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 100, 'Игровые параметры ', Color.WHITE)
    )
    volume_slider = VolumeSlider()
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

