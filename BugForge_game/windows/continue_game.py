import os
import json
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from objects.groups_objects import HealthBar
from objects.groups_objects import player
from structures_and_parameters.parameters_game import ActionParams
from .game_window.game_loop import main_game_loop


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
        player.score = save_data["score_money"]
        player.speed_move = save_data["speed_hero"]
        Rooms.NUMBER_LEVEL = save_data["number_level"]
        ActionParams.FLAG_UPPER_HEALTH_BAR = save_data["health_bar"]
        Rooms.FLAG_LOAD_SAVE = True
    main_game_loop()
