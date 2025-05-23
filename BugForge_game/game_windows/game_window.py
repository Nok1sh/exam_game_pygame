import pygame
import json
from structures_and_parameters.structures_on_each_level import Rooms
from structures_and_parameters.enemies_on_each_levels import GetEnemiesStructure
from structures_and_parameters.parameters_game import WindowParams, Color, ActionParams
from objects.groups_objects import (player_group, walls_group, add_magic_ball, magic_balls, bars, projectiles,
                                    portal, portal_stand, player, restart_game, Floor,
                                    text_score_money, HealthBar)
from window_options import options_in_game
pygame.init()


def main_game_loop() -> None:
    restart_game()
    Rooms.FLAG_LOAD_SAVE = False
    enemies_by_room = GetEnemiesStructure.ENEMIES
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
        if not player.is_life or WindowParams.FLAG_RETURN_TO_MAIN_MENU:
            WindowParams.FLAG_RETURN_TO_MAIN_MENU = False
            return

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
            with open("../exam_game_pygame/saves/save.json", "w", encoding="utf-8") as file:
                json.dump(save_to_continue_level, file, indent=4, ensure_ascii=False)

        WindowParams.SCREEN.fill(Color.BLACK)
        #Floor.floor(WindowParams.SCREEN)
        walls_room = walls_group(Rooms.ROOM)
        current_enemies = enemies_by_room.get(Rooms.ROOM)
        # current_enemies = None
        current_portal = Rooms.PORTAL_AND_STAND.get(Rooms.ROOM)
        current_structures = Rooms.LEVEL_STRUCTURE.get(Rooms.ROOM)
        tent_structure = Rooms.TENT.get(Rooms.ROOM)
        if current_enemies:
            if current_structures:
                current_enemies.update(player, walls_room, magic_balls, projectiles, current_structures["coins"], current_structures["barrels"], current_structures["columns"])
                projectiles.update(current_enemies, player, walls_room, current_structures["barrels"], current_structures["columns"])
                current_enemies.draw(WindowParams.SCREEN)
                Rooms.DOORS.draw(WindowParams.SCREEN)
                Rooms.DOORS_FLAG = True
            else:
                current_enemies.update(player, walls_room, magic_balls, projectiles, current_structures["coins"])
                current_enemies.draw(WindowParams.SCREEN)
                projectiles.update(player, walls_room)
        else:
            Rooms.DOORS_FLAG = False

        if tent_structure:
            tent_structure.draw(WindowParams.SCREEN)

        if current_structures:
            current_structures["barrels"].draw(WindowParams.SCREEN)
            current_structures["barrels"].update(magic_balls, projectiles, player, current_structures["coins"], current_structures["potions"])
            current_structures["coins"].draw(WindowParams.SCREEN)
            current_structures["coins"].update()
            current_structures["columns"].draw(WindowParams.SCREEN)
            current_structures["columns"].update(magic_balls)
            current_structures["potions"].draw(WindowParams.SCREEN)

            player_group.update(player, barrels=current_structures["barrels"], moneys=current_structures["coins"], columns=current_structures["columns"], potions=current_structures["potions"])
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
        magic_balls.update(walls_room)
        bars.update()
        magic_balls.draw(WindowParams.SCREEN)
        projectiles.draw(WindowParams.SCREEN)
        player_group.draw(WindowParams.SCREEN)
        walls_group(Rooms.ROOM).draw(WindowParams.SCREEN)
        bars.draw(WindowParams.SCREEN)
        text_score_money.draw_score_money(player.score, WindowParams.SCREEN)
        pygame.display.flip()
        ActionParams.CLOCK.tick(ActionParams.FPS)


def continue_from_the_save():
    with open("../exam_game_pygame/saves/save.json", "r", encoding="utf-8") as file:
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
