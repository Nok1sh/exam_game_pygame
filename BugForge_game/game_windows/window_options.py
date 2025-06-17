import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, ActionParams, Music
from objects.ui.bars import HealthBar
from objects.ui.text import TextOnWindowForOptions
from objects.ui.store import StoreMenu, Trader
from objects.ui.buttons import ButtonMenu, ButtonBack, ButtonAction
from objects.ui.volumeslider import VolumeSlider
from objects.world_objects.world_structures import BackgroundOptions
from structures_and_parameters.parameters_rooms_and_structures import Rooms

options_screen = pygame.display.set_mode(
    (WindowParams.WIDTH, WindowParams.HEIGHT),
)
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


def run_music() -> None:
    Music.FLAG_RUN_MUSIC = False
    Music.FLAG_SWAP_MUSIC = True


def stop_music() -> None:
    pygame.mixer.music.stop()
    Music.FLAG_RUN_MUSIC = True
    Music.FLAG_SWAP_MUSIC = False


def options_main_menu() -> None:
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu('Полный экран', WindowParams.HEIGHT // 2 - 200, x=WindowParams.WIDTH//2 - 180, button_call=fullscreen, width=300, height=75),
        ButtonMenu(f'Оконный режим', WindowParams.HEIGHT // 2 - 200, x=WindowParams.WIDTH//2 + 180, button_call=window_screen, width=300, height=75),
        ButtonMenu(f'Увеличенное здоровье', WindowParams.HEIGHT // 2, x=WindowParams.WIDTH//2 - 180, button_call=change_health_bar_big, width=300, height=75),
        ButtonMenu(f'Уменьшенное здоровье', WindowParams.HEIGHT // 2, x=WindowParams.WIDTH//2 + 180, button_call=change_health_bar_small, width=300, height=75),
    ButtonMenu(f'Включить музыку', WindowParams.HEIGHT // 2 + 100, x=WindowParams.WIDTH // 2 - 180, button_call=run_music, width=300, height=75),
    ButtonMenu(f'Выключить музыку', WindowParams.HEIGHT // 2 + 100, x=WindowParams.WIDTH // 2 + 180, button_call=stop_music, width=300, height=75)
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
        BackgroundOptions.draw(options_screen)
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

        volume_slider.draw(options_screen)

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


def parameters_in_game() -> None:
    buttons_options_group = pygame.sprite.Group(
        ButtonMenu(f'Включить музыку', WindowParams.HEIGHT // 2 - 100, x=WindowParams.WIDTH // 2 - 180,
                   button_call=run_music, width=300, height=75),
        ButtonMenu(f'Выключить музыку', WindowParams.HEIGHT // 2 - 100, x=WindowParams.WIDTH // 2 + 180,
                   button_call=stop_music, width=300, height=75)
    )
    button_back_group = pygame.sprite.Group(
        ButtonBack('Назад', WindowParams.HEIGHT // 2 + 325, 200)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 200, 'Игровые параметры ', Color.WHITE)
    )
    volume_slider = VolumeSlider(y=WindowParams.HEIGHT//2+100)
    while True:
        BackgroundOptions.draw(options_screen)
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

        volume_slider.draw(options_screen)

        for btn in text_options_group:
            btn.draw_text(options_screen)
        for btn in buttons_options_group:
            btn.draw(options_screen)
        for btn in button_back_group:
            btn.draw(options_screen)
        pygame.display.flip()


def options_in_game() -> None:
    global continue_game, back_to_main_menu
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
        BackgroundOptions.draw(options_screen)
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


def information_menu() -> None:
    button_back_group = pygame.sprite.Group(
        ButtonBack('Назад', WindowParams.HEIGHT // 2 + 325, 200)
    )
    text_information_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 320, 'Информация про игру', Color.WHITE),
        TextOnWindowForOptions(120, WindowParams.HEIGHT // 2 - 260, '1. Управление:', Color.WHITE, 32),
        TextOnWindowForOptions(150, WindowParams.HEIGHT // 2 - 210, 'W - идти вперёд', Color.WHITE, 32),
        TextOnWindowForOptions(140, WindowParams.HEIGHT // 2 - 160, 'S - идти назад', Color.WHITE, 32),
        TextOnWindowForOptions(140, WindowParams.HEIGHT // 2 - 110, 'A - идти влево', Color.WHITE, 32),
        TextOnWindowForOptions(150, WindowParams.HEIGHT // 2 - 60, 'D - идти вправо', Color.WHITE, 32),
        TextOnWindowForOptions(190, WindowParams.HEIGHT // 2, 'Зажимая две кнопки,', Color.WHITE, 32),
        TextOnWindowForOptions(170, WindowParams.HEIGHT // 2 + 40, 'идти по диагонали', Color.WHITE, 32),
        TextOnWindowForOptions(160, WindowParams.HEIGHT // 2 + 100, 'SPACE - стрелять', Color.WHITE, 32),
        TextOnWindowForOptions(220, WindowParams.HEIGHT // 2 + 140, 'в направлении движения', Color.WHITE, 32),
        TextOnWindowForOptions(180, WindowParams.HEIGHT // 2 + 200, 'E - взаимодействие', Color.WHITE, 32),
        TextOnWindowForOptions(150, WindowParams.HEIGHT // 2 + 240, 'со структурами', Color.WHITE, 32),
        TextOnWindowForOptions(WindowParams.WIDTH//2, WindowParams.HEIGHT // 2 - 260, '2. Важные моменты:', Color.WHITE, 32),
        TextOnWindowForOptions(WindowParams.WIDTH // 2 + 140, WindowParams.HEIGHT // 2 - 220, '1) Для перехода между уровнями используется портал', Color.WHITE, 24),
        TextOnWindowForOptions(WindowParams.WIDTH // 2 + 175, WindowParams.HEIGHT // 2 - 180, 'для его активации нужно убить всех противников на уровне', Color.WHITE, 24),
        TextOnWindowForOptions(WindowParams.WIDTH // 2 + 215, WindowParams.HEIGHT // 2 - 140,'2) При переходе на новый уровень, противники становятся сильнее',Color.WHITE, 24),
        TextOnWindowForOptions(WindowParams.WIDTH // 2 + 200, WindowParams.HEIGHT // 2 - 100,'3) При переходе на новый уровень, цены у торговца возрастают', Color.WHITE, 24),
        TextOnWindowForOptions(WindowParams.WIDTH // 2 + 155, WindowParams.HEIGHT // 2 - 60, '4) При переходе на новый уровень, сохраняется прогресс', Color.WHITE, 24),
    )
    while True:
        BackgroundOptions.draw(options_screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for back in button_back_group:
                back.type_to_button(event)
                if back.flag_back:
                    return

        for btn in text_information_group:
            btn.draw_text(options_screen)
        for btn in button_back_group:
            btn.draw(options_screen)
        pygame.display.flip()


def store_menu(player) -> None:
    def update_score_image():
        list(text_options_group)[-1].kill()
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
        ButtonBack('Назад', WindowParams.HEIGHT // 2 + 250, 300)
    )
    text_options_group = pygame.sprite.Group(
        TextOnWindowForOptions(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 300, 'CURIOSITY SHOP', Color.WHITE),
        TextOnWindowForOptions(WindowParams.WIDTH//2+250, WindowParams.HEIGHT // 2 - 230, f'Приветствую тебя, путник,', Color.WHITE, 28),
        TextOnWindowForOptions(WindowParams.WIDTH//2+180, WindowParams.HEIGHT // 2 - 200, f'не желаешь прикупить', Color.WHITE, 28),
        TextOnWindowForOptions(WindowParams.WIDTH // 2 + 230, WindowParams.HEIGHT // 2 - 170, f'чего-нибудь из моих товаров?', Color.WHITE, 28),
        TextOnWindowForOptions(200, WindowParams.HEIGHT // 2 - 300, f'Твои монеты: {player.score}', Color.WHITE, 28)
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

