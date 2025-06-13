import pygame
import os
import json
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from structures_and_parameters.groups_of_enemies_model import GetEnemiesStructure
from structures_and_parameters.parameters_game import WindowParams, ActionParams
from objects.groups_objects import (player_group, walls_group, add_magic_ball, magic_balls_hero, bars, magic_ball_enemy,
                                    portal, portal_stand, player, restart_game,
                                    text_score_money, HealthBar, player_render_group)
from objects.world_objects.world_structures import Floor
from game_windows.window_options import options_in_game
pygame.init()


def main_game_loop() -> None:
    """
    Gameplay processing function
    """
    Floor.init(WindowParams.WIDTH, WindowParams.HEIGHT)
    restart_game()
    Rooms.FLAG_LOAD_SAVE = False
    enemies_by_room = GetEnemiesStructure.ENEMIES
    Rooms.fade_swap_level()
    Floor.draw(WindowParams.SCREEN)
    current_room = -1
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (pygame.time.get_ticks() - ActionParams.DELAY_MAGIC_BALLS >= ActionParams.LAST_MAGIC_BALLS) and player.mana_pool > 0:
                        add_magic_ball(player.line_move, player.rect.center)
                        player.mana_pool -= 1
                        ActionParams.LAST_MAGIC_BALLS = pygame.time.get_ticks()
                elif event.key == pygame.K_ESCAPE:
                    options_in_game()

        # check gameplay
        if not player.is_life or WindowParams.FLAG_RETURN_TO_MAIN_MENU:
            WindowParams.FLAG_RETURN_TO_MAIN_MENU = False
            return

        # save each passing the level
        if Rooms.FLAG_SWAP_LEVEL:
            walls_room = walls_group(Rooms.ROOM)
            GetEnemiesStructure.update_level()
            enemies_by_room = GetEnemiesStructure.ENEMIES
            Rooms.FLAG_SWAP_LEVEL = False
            save_to_continue_level = {
                "player_attack_damage": player.damage,
                "player_health": player.health_bar,
                "health_bar": ActionParams.FLAG_UPPER_HEALTH_BAR,
                "score_money": player.score,
                "speed_hero": player.speed_move,
                "number_level": Rooms.NUMBER_LEVEL
            }
            if not os.path.exists("saves"):
                os.mkdir("saves")
            with open("saves/save.json", "w", encoding="utf-8") as file:
                json.dump(save_to_continue_level, file, indent=4, ensure_ascii=False)

        if current_room != Rooms.ROOM:
            current_room = Rooms.ROOM
            walls_room = walls_group(Rooms.ROOM)
            current_enemies = enemies_by_room.get(Rooms.ROOM)
            current_portal = Rooms.PORTAL_AND_STAND.get(Rooms.ROOM)
            current_structures = Rooms.LEVEL_STRUCTURE.get(Rooms.ROOM)
            tent_structure = Rooms.TENT.get(Rooms.ROOM)
        Floor.draw(WindowParams.SCREEN)

        # update enemies for each room
        if current_enemies:
            if current_structures:
                current_enemies.update(player, walls_room, magic_balls_hero, magic_ball_enemy, current_structures["coins"], current_structures["barrels"], current_structures["columns"])
                magic_ball_enemy.update(walls_room, current_enemies, current_structures["barrels"], current_structures["columns"], player=player, coins=current_structures["coins"], potions=current_structures["potions"])
                Rooms.DOORS.draw(WindowParams.SCREEN)
                Rooms.DOORS_FLAG = True
            else:
                current_enemies.update(player, walls_room, magic_balls_hero, magic_ball_enemy, current_structures["coins"])
                magic_ball_enemy.update(walls_room, player=player)
        else:
            Rooms.DOORS_FLAG = False

        # update shop on each level
        if tent_structure:
            tent_structure.draw(WindowParams.SCREEN)

        # update structures for each room
        if current_structures:
            current_structures["barrels"].draw(WindowParams.SCREEN)
            current_structures["coins"].draw(WindowParams.SCREEN)
            current_structures["coins"].update()
            current_structures["columns"].draw(WindowParams.SCREEN)
            current_structures["potions"].draw(WindowParams.SCREEN)

            player_group.update(player, barrels=current_structures["barrels"], moneys=current_structures["coins"], columns=current_structures["columns"], potions=current_structures["potions"])
            magic_balls_hero.update(walls_room, barrels=current_structures["barrels"],
                                    columns=current_structures["columns"], coins=current_structures["coins"],
                                    potions=current_structures["potions"])
        else:
            magic_balls_hero.update(walls_room)

        # update portal and portal stand
        if current_portal:
            portal_stand.draw(WindowParams.SCREEN)
            if [len(group) for group in enemies_by_room.values()].count(0) == len(enemies_by_room.values()):
                portal.update()
                portal.draw(WindowParams.SCREEN)
                player_group.update(player, walls=walls_room, portal=portal, tent=tent_structure)
            else:
                player_group.update(player, walls=walls_room, tent=tent_structure)
        else:
            player_group.update(player, walls=walls_room, tent=tent_structure)

        # update other objects
        bars.update()
        player_render_group.update(player)
        player_render_group.draw(WindowParams.SCREEN)
        magic_balls_hero.draw(WindowParams.SCREEN)
        magic_ball_enemy.draw(WindowParams.SCREEN)
        walls_group(Rooms.ROOM).draw(WindowParams.SCREEN)
        bars.draw(WindowParams.SCREEN)
        text_score_money.draw_text(player.score, WindowParams.SCREEN)

        pygame.display.flip()
        ActionParams.CLOCK.tick(ActionParams.FPS)
        fps = ActionParams.CLOCK.get_fps()
        pygame.display.set_caption(f"BugForge - FPS: {int(fps)}")


def continue_from_the_save() -> None:
    """
    Function if the user chooses to continue the game from save
    """
    if not os.path.exists('saves') or not os.path.exists('saves/save.json'):
        return
    with open("saves/save.json", "r", encoding="utf-8") as file:
        save_data = json.load(file)
        player.damage = save_data["player_attack_damage"]
        player.health_bar = save_data["player_health"]
        HealthBar.FLAG_SWAP = True
        ActionParams.FLAG_UPPER_HEALTH_BAR = save_data["player_health"]
        player.score = save_data["score_money"]
        player.speed_move = save_data["speed_hero"]
        Rooms.NUMBER_LEVEL = save_data["number_level"]
        ActionParams.FLAG_UPPER_HEALTH_BAR = save_data["health_bar"]
        Rooms.FLAG_LOAD_SAVE = True
    main_game_loop()
