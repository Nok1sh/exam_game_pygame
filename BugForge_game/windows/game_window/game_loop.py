import pygame
from .game_logic import update_game_state, update_objects
from .game_render import draw_game_scene
from .game_audio import handle_music
from objects.groups_objects import restart_game, player
from windows.options_windows.options_in_game import options_in_game
from structures_and_parameters.parameters_game import WindowParams, ActionParams


def main_game_loop() -> None:
    restart_game()
    clock = ActionParams.CLOCK
    current_room = -1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    from .game_logic import player_attack
                    player_attack()
                elif event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.pause()
                    options_in_game()
                    pygame.mixer.music.unpause()

        if not player.is_life or WindowParams.FLAG_RETURN_TO_MAIN_MENU:
            pygame.mixer.music.stop()
            WindowParams.FLAG_RETURN_TO_MAIN_MENU = False
            return

        current_room = update_game_state(current_room)
        draw_game_scene(WindowParams.SCREEN)
        update_objects()
        handle_music()

        pygame.display.flip()
        clock.tick(ActionParams.FPS)
        fps = clock.get_fps()
        pygame.display.set_caption(f"BugForge - FPS: {int(fps)}")


