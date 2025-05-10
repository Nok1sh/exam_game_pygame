import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, ActionParams
from objects.interface_objects import TextOnWindowForOptions, ButtonMenu, ButtonBack, ButtonAction, StoreMenu, Trader
import importlib
from structures_and_parameters import rooms
from structures_and_parameters.structures_on_each_level import Rooms

options_screen = pygame.display.set_mode(
    (WindowParams.WIDTH, WindowParams.HEIGHT)
)


def fullscreen() -> None:
    WindowParams.update_screen(size_fullscreen=True)
    importlib.reload(room_structures)


def window_screen() -> None:
    WindowParams.update_screen()
    importlib.reload(room_structures)


def options_main_menu() -> None:
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu('Fullscreen', WindowParams.HEIGHT // 2 - 50, button_call=fullscreen),
        ButtonMenu(f'Windowed Mode', WindowParams.HEIGHT // 2 + 100, button_call=window_screen)
    )
    button_back_group = pygame.sprite.Group(
        ButtonBack('Back', WindowParams.HEIGHT // 2 + 300, 200)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 200, 'Resolution', Color.WHITE)
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


continue_game: bool = False
back_to_main_menu: bool = False


def continue_game_button() -> None:
    global continue_game
    continue_game = True


def return_to_main_menu() -> None:
    global back_to_main_menu
    back_to_main_menu = True
    WindowParams.FLAG_RETURN_TO_MAIN_MENU = True


def options_in_game() -> None:
    global continue_game, back_to_main_menu
    continue_game = False
    back_to_main_menu = False
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu('Продолжить', WindowParams.HEIGHT // 2 - 150, continue_game_button),
        ButtonMenu('Вернуться в главное меню', WindowParams.HEIGHT // 2, return_to_main_menu),
        ButtonMenu(f'Выйти из игры', WindowParams.HEIGHT // 2 + 150, pygame.quit)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 300, 'Настройки', Color.WHITE)
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
                if back_to_main_menu:
                    return
        for btn in text_options_group:
            btn.draw_text(options_screen)
        for btn in buttons_options_group:
            btn.draw(options_screen)
        pygame.display.flip()


def store_menu(player) -> None:
    def update_score_image():
        list(text_options_group)[1].kill()
        text_options_group.add(TextOnWindowForOptions(200, WindowParams.HEIGHT // 2 - 300, f'Твои монеты: {player.score}', Color.WHITE, 28))

    def update_damage():
        if player.score >= Rooms.COST_UPDATE_DAMAGE:
            player.score -= Rooms.COST_UPDATE_DAMAGE
            player.damage += 1
            update_score_image()

    def update_speed():
        if player.score >= Rooms.COST_UPDATE_SPEED:
            player.score -= Rooms.COST_UPDATE_SPEED
            player.speed_move += 1
            update_score_image()

    def update_recovery_mana():
        if player.score >= Rooms.COST_UPDATE_RECOVERED_MANA:
            player.score -= Rooms.COST_UPDATE_RECOVERED_MANA
            ActionParams.RECOVERY_MANA_BAR -= 500
            update_score_image()

    def recovery_health():
        if player.score >= Rooms.COST_RECOVERY_HEALTH:
            player.score -= Rooms.COST_RECOVERY_HEALTH
            player.health_bar = player.max_health
            update_score_image()

    button_back_group = pygame.sprite.Group(
        ButtonBack('Back', WindowParams.HEIGHT // 2 + 250, 300)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 300, 'CURIOSITY SHOP', Color.WHITE),
        TextOnWindowForOptions(200, WindowParams.HEIGHT // 2 - 300, f'Твои монеты: {player.score}', Color.WHITE, 28),
        TextOnWindowForOptions(WindowParams.WIDTH//2+250, WindowParams.HEIGHT // 2 - 200, f'Приветствую тебя, путник, не желаешь прикупить', Color.WHITE, 28),
        TextOnWindowForOptions(WindowParams.WIDTH//2+180, WindowParams.HEIGHT // 2 - 170, f'чего-нибудь из моих товаров?', Color.WHITE, 28)
    )
    buttons_attributes = pygame.sprite.Group(
        ButtonAction(f'Увеличить урон на 1 за {Rooms.COST_UPDATE_DAMAGE} монет', WindowParams.HEIGHT // 2 - 200, update_damage, 350),
        ButtonAction(f'Увеличить скорость на 1 за {Rooms.COST_UPDATE_SPEED} монет', WindowParams.HEIGHT // 2 - 90, update_speed, 350),
        ButtonAction(f'Ускорить регенерацию маны за {Rooms.COST_UPDATE_RECOVERED_MANA} монет', WindowParams.HEIGHT // 2 + 20, update_recovery_mana, 350),
        ButtonAction(f'Восстановить всё здоровье за {Rooms.COST_RECOVERY_HEALTH} монет',WindowParams.HEIGHT // 2 + 130, recovery_health, 350)
    )
    store_menu_img = pygame.sprite.Group(StoreMenu())

    trader = pygame.sprite.Group(Trader())
    while True:
        store_menu_img.draw(WindowParams.SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for back in button_back_group:
                back.type_to_button(event)
                if back.flag_back:
                    return
            for button in buttons_attributes:
                button.type_to_button(event)

        trader.draw(WindowParams.SCREEN)
        for btn in text_options_group:
            btn.draw_text(options_screen)
        for btn in button_back_group:
            btn.draw(options_screen)
        for button in buttons_attributes:
            button.draw(options_screen)

        pygame.display.flip()
        ActionParams.CLOCK.tick(ActionParams.FPS)

