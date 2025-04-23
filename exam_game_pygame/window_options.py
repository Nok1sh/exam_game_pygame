import pygame
from parameters_game import WindowParams, Color
from interface_objects import TextOnWindow, ButtonMainMenu, ButtonBack
import importlib
import room_structures


options_screen = pygame.display.set_mode(
    (WindowParams.WIDTH, WindowParams.HEIGHT)
)


def fullscreen():
    WindowParams.update_screen(size_fullscreen=True)
    importlib.reload(room_structures)


def window_screen():
    WindowParams.update_screen()
    importlib.reload(room_structures)


def options_main_menu():
    buttons_options_group = pygame.sprite.Group(
        ButtonMainMenu('Fullscreen', WindowParams.HEIGHT//2-50, fullscreen),
        ButtonMainMenu(f'Windowed Mode', WindowParams.HEIGHT // 2 + 100, window_screen)
    )
    button_back_group = pygame.sprite.Group(
        ButtonBack('Back', 200, WindowParams.HEIGHT // 2 + 300)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindow(WindowParams.WIDTH//2, WindowParams.HEIGHT//2-200, 'Resolution', Color.WHITE)
    )
    while True:
        options_screen.fill(Color.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for btn in buttons_options_group:
                btn.type_to_button(event)
            for back in button_back_group:
                back.type_to_button(event)
                if back.flag_back:
                    return

        for btn in text_options_group:
            btn.draw_text(options_screen)
        for btn in buttons_options_group:
            btn.draw(options_screen)
        for btn in button_back_group:
            btn.draw(options_screen)
        pygame.display.flip()


continue_game = False


def continue_game_button():
    global continue_game
    continue_game = True


def options_in_game():
    global continue_game
    continue_game = False
    buttons_options_group = pygame.sprite.Group(
        ButtonMainMenu('Продолжить', WindowParams.HEIGHT//2-50, continue_game_button),
        ButtonMainMenu(f'Выйти из игры', WindowParams.HEIGHT // 2 + 100, pygame.quit)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindow(WindowParams.WIDTH//2, WindowParams.HEIGHT//2-200, 'Настройки', Color.WHITE)
    )
    while True:
        options_screen.fill(Color.BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for btn in buttons_options_group:
                btn.type_to_button(event)
                if continue_game:
                    return
        for btn in text_options_group:
            btn.draw_text(options_screen)
        for btn in buttons_options_group:
            btn.draw(options_screen)
        pygame.display.flip()