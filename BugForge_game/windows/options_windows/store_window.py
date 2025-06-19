import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, ActionParams
from objects.ui.text import TextOnWindowForOptions
from objects.ui.store import StoreMenu, Trader
from objects.ui.buttons import ButtonBack, ButtonAction
from objects.world_objects.background_options import BackgroundOptions
from structures_and_parameters.parameters_rooms_and_structures import Rooms


def store_menu(player) -> None:
    """
    Game store window
    """
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
        BackgroundOptions.draw(WindowParams.SCREEN)
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
            btn.draw_text(WindowParams.OPTION_SCREEN)
        for btn in button_back_group:
            btn.draw(WindowParams.OPTION_SCREEN)
        for button in buttons_attributes:
            button.draw(WindowParams.OPTION_SCREEN)

        pygame.display.flip()
        ActionParams.CLOCK.tick(ActionParams.FPS)