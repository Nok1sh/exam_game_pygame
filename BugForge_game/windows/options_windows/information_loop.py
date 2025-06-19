import pygame
from structures_and_parameters.parameters_game import WindowParams, Color
from objects.ui.text import TextOnWindowForOptions
from objects.ui.buttons import ButtonBack
from objects.world_objects.background_options import BackgroundOptions


def information_menu() -> None:
    """
    Window with important game information
    """
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
        BackgroundOptions.draw(WindowParams.OPTION_SCREEN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            for back in button_back_group:
                back.type_to_button(event)
                if back.flag_back:
                    return

        for btn in text_information_group:
            btn.draw_text(WindowParams.OPTION_SCREEN)
        for btn in button_back_group:
            btn.draw(WindowParams.OPTION_SCREEN)
        pygame.display.flip()