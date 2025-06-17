from structures_and_parameters.parameters_game import Music
from structures_and_parameters.groups_of_enemies_model import RangeBossEnemy
from structures_and_parameters.parameters_rooms_and_structures import Rooms


def handle_music() -> None:
    if Rooms.CURRENT_ENEMIES and isinstance(list(Rooms.CURRENT_ENEMIES)[0], RangeBossEnemy):
        if not Music.FLAG_SWAP_MUSIC:
            Music.FLAG_SWAP_MUSIC = True
            Music.swap_music(Music.BOSS_BATTLE)

    elif Music.FLAG_SWAP_MUSIC:
        Music.swap_music(Music.BASE_BACKGROUND)
        Music.FLAG_SWAP_MUSIC = False


