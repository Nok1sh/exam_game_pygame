import pygame
from structures_and_parameters.parameters_game import WindowParams, Color, Rooms, ActionParams
from objects.groups_objects import (player_group, walls_group, add_magic_ball, magic_balls, bars, projectiles,
                                    portal_and_stand, portal, portal_stand, player, restart_game, Floor,
                                    text_score_money)
from window_options import options_in_game
pygame.init()


def main_game_loop() -> None:
    enemies_by_room, other_structures = restart_game()
    # flag_return_to_main_menu: bool = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (pygame.time.get_ticks() - ActionParams.DELAY_MAGIC_BALLS >= ActionParams.LAST_MAGIC_BALLS) and player.mana_pool > 0:
                        add_magic_ball(player.line_move, player.rect.x, player.rect.y)
                        player.mana_pool -= 1
                        ActionParams.LAST_MAGIC_BALLS = pygame.time.get_ticks()
                elif event.key == pygame.K_ESCAPE:
                    options_in_game()
        if not player.is_life or WindowParams.FLAG_RETURN_TO_MAIN_MENU:
            WindowParams.FLAG_RETURN_TO_MAIN_MENU = False
            return

        if Rooms.FLAG_SWAP_LEVEL:
            walls_room = walls_group(Rooms.ROOM)
            Rooms.FLAG_SWAP_LEVEL = False

        WindowParams.SCREEN.fill(Color.BLACK)
        #Floor.floor(WindowParams.SCREEN)
        walls_room = walls_group(Rooms.ROOM)
        #current_enemies = enemies_by_room.get(Rooms.ROOM)
        current_enemies = None
        current_portal = portal_and_stand.get(Rooms.ROOM)
        current_structures = other_structures.get(Rooms.ROOM)

        if current_enemies:
            if current_structures:
                current_enemies.update(player, walls_room, magic_balls, projectiles, current_structures)
                current_enemies.draw(WindowParams.SCREEN)
            else:
                current_enemies.update(player, walls_room, magic_balls, projectiles)
                current_enemies.draw(WindowParams.SCREEN)

        if current_structures:
            current_structures["barrels"].draw(WindowParams.SCREEN)
            current_structures["barrels"].update(magic_balls, player, current_structures["coins"])
            current_structures["coins"].draw(WindowParams.SCREEN)
            current_structures["coins"].update()

            player_group.update(barrels=current_structures["barrels"], moneys=current_structures["coins"])
        if current_portal:
            portal_stand.draw(WindowParams.SCREEN)
            if [len(group) for group in enemies_by_room.values()].count(0) == len(enemies_by_room.values()):
                portal.update()
                portal.draw(WindowParams.SCREEN)
                player_group.update(walls=walls_room, portal=portal)
            else:
                player_group.update(walls=walls_room)
        else:
            player_group.update(walls=walls_room)
        projectiles.update(player, walls_room)
        magic_balls.update(walls_room)
        bars.update()
        projectiles.draw(WindowParams.SCREEN)
        player_group.draw(WindowParams.SCREEN)
        magic_balls.draw(WindowParams.SCREEN)
        walls_group(Rooms.ROOM).draw(WindowParams.SCREEN)
        bars.draw(WindowParams.SCREEN)
        text_score_money.draw_score_money(player.score, WindowParams.SCREEN)
        pygame.display.flip()
        ActionParams.CLOCK.tick(ActionParams.FPS)
