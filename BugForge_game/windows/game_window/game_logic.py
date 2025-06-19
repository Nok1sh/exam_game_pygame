import pygame
import os
import json
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from structures_and_parameters.environment.groups_of_enemies_model import GetEnemiesStructure
from structures_and_parameters.parameters_game import ActionParams
from structures_and_parameters.get_structures_and_enemies_on_level import get_objects
from objects.groups_objects import player_group, walls_group, add_magic_ball, magic_balls_hero, magic_ball_enemy, player


def player_attack() -> None:
    """
    Generates the player's projectiles
    """
    if (pygame.time.get_ticks() - ActionParams.DELAY_MAGIC_BALLS >= ActionParams.LAST_MAGIC_BALLS) and player.mana_pool > 0:
        add_magic_ball(player.line_move, player.rect.center)
        player.mana_pool -= 1
        ActionParams.LAST_MAGIC_BALLS = pygame.time.get_ticks()


def update_game_state(current_room) -> int:
    """
    Updating the save settings and objects when the room changes
    """
    if Rooms.FLAG_SWAP_LEVEL:
        walls_room = walls_group(Rooms.ROOM)
        GetEnemiesStructure.update_level()
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
        Rooms.WALLS_ROOM = walls_group(Rooms.ROOM)
        Rooms.CURRENT_ENEMIES = get_objects(GetEnemiesStructure.ENEMIES, Rooms.ROOM)
        Rooms.CURRENT_PORTAL = Rooms.PORTAL_AND_STAND.get(Rooms.ROOM)
        Rooms.CURRENT_STRUCTURES = get_objects(Rooms.LEVEL_STRUCTURE, Rooms.ROOM, "structures")
        Rooms.TENT_STRUCTURE = Rooms.TENT.get(Rooms.ROOM)
    return Rooms.ROOM


def update_objects() -> None:
    if Rooms.CURRENT_STRUCTURES:
        Rooms.CURRENT_STRUCTURES["coins"].update()

    if Rooms.CURRENT_ENEMIES:
        if Rooms.CURRENT_STRUCTURES:
            Rooms.CURRENT_ENEMIES.update(player, Rooms.WALLS_ROOM, magic_balls_hero, magic_ball_enemy,
                                         Rooms.CURRENT_STRUCTURES["coins"], Rooms.CURRENT_STRUCTURES["barrels"],
                                         Rooms.CURRENT_STRUCTURES["columns"])
            magic_ball_enemy.update(Rooms.WALLS_ROOM, Rooms.CURRENT_ENEMIES,
                                    Rooms.CURRENT_STRUCTURES["barrels"], Rooms.CURRENT_STRUCTURES["columns"],
                                    player=player, coins=Rooms.CURRENT_STRUCTURES["coins"],
                                    potions=Rooms.CURRENT_STRUCTURES["potions"])
            Rooms.DOORS_FLAG = True
        else:
            Rooms.CURRENT_ENEMIES.update(player, Rooms.WALLS_ROOM, magic_balls_hero, magic_ball_enemy)
            magic_ball_enemy.update(Rooms.WALLS_ROOM, player=player)
    else:
        Rooms.DOORS_FLAG = False
    player_group.update(player, walls=Rooms.WALLS_ROOM, portal=Rooms.CURRENT_PORTAL, tent=Rooms.TENT_STRUCTURE,
                        barrels=Rooms.CURRENT_STRUCTURES.get("barrels") if Rooms.CURRENT_STRUCTURES else None,
                        moneys=Rooms.CURRENT_STRUCTURES.get("coins") if Rooms.CURRENT_STRUCTURES else None,
                        columns=Rooms.CURRENT_STRUCTURES.get("columns") if Rooms.CURRENT_STRUCTURES else None,
                        potions=Rooms.CURRENT_STRUCTURES.get("potions") if Rooms.CURRENT_STRUCTURES else None)
    magic_balls_hero.update(Rooms.WALLS_ROOM,
                            barrels=Rooms.CURRENT_STRUCTURES["barrels"] if Rooms.CURRENT_STRUCTURES else None,
                            columns=Rooms.CURRENT_STRUCTURES["columns"] if Rooms.CURRENT_STRUCTURES else None,
                            coins=Rooms.CURRENT_STRUCTURES["coins"] if Rooms.CURRENT_STRUCTURES else None,
                            potions=Rooms.CURRENT_STRUCTURES["potions"] if Rooms.CURRENT_STRUCTURES else None)

