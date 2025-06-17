from structures_and_parameters.parameters_rooms_and_structures import Rooms
from objects.groups_objects import (player_render_group, magic_balls_hero, magic_ball_enemy,
                                    bars, text_score_money, walls_group, portal_stand)
from structures_and_parameters.parameters_game import WindowParams
from structures_and_parameters.groups_of_enemies_model import GetEnemiesStructure
from objects.world_objects.world_structures import Floor
from objects.groups_objects import player, portal

Floor.init(WindowParams.WIDTH, WindowParams.HEIGHT)


def draw_game_scene(screen) -> None:
    Floor.draw(screen)
    if Rooms.TENT_STRUCTURE:
        Rooms.TENT_STRUCTURE.draw(screen)

    if Rooms.CURRENT_STRUCTURES:
        Rooms.CURRENT_STRUCTURES["barrels"].draw(screen)
        Rooms.CURRENT_STRUCTURES["coins"].draw(screen)
        Rooms.CURRENT_STRUCTURES["columns"].draw(screen)
        Rooms.CURRENT_STRUCTURES["potions"].draw(screen)

    if Rooms.CURRENT_PORTAL:
        portal_stand.draw(screen)
        if [len(group) for group in GetEnemiesStructure.ENEMIES.values()].count(0) == len(GetEnemiesStructure.ENEMIES.values()):
            portal.update()
            portal.draw(screen)

    if Rooms.DOORS_FLAG:
        Rooms.DOORS.draw(screen)

    player_render_group.update(player)
    player_render_group.draw(screen)
    magic_balls_hero.draw(screen)
    magic_ball_enemy.draw(screen)
    walls_group(Rooms.ROOM).draw(screen)
    bars.update()
    bars.draw(screen)
    text_score_money.draw_text(player.score, screen)
