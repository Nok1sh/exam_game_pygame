import pygame
from typing import Dict
from structures_and_parameters.parameters_game import WindowParams
from structures_and_parameters.parameters_rooms_and_structures import Rooms
from objects.action_objects.enemies_direction.melee_enemy_direction.melee_enemy import MeleeEnemy
from objects.action_objects.enemies_direction.range_enemy_direction.range_enemy import RangeEnemy
from objects.action_objects.enemies_direction.boss_enemy_direction.boss_range_enemy import RangeBossEnemy


class EnemiesStructure(pygame.sprite.Sprite):
    @staticmethod
    def get_enemies_on_level(number_level: int) -> Dict[int, pygame.sprite.Group]:
        if number_level == 1:
            enemies_by_room = {1: pygame.sprite.Group(
                RangeEnemy(100, 100),
                MeleeEnemy(WindowParams.WIDTH//2 - 200, WindowParams.HEIGHT - 150)
            ),
                2: pygame.sprite.Group(
                    MeleeEnemy(200, WindowParams.HEIGHT//2-200)
                ),
                8: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH - 150, 100),
                    MeleeEnemy(WindowParams.WIDTH - 150, WindowParams.HEIGHT - 150)
                ),
                12: pygame.sprite.Group(
                    RangeEnemy(100, WindowParams.HEIGHT-150),
                    RangeEnemy(WindowParams.WIDTH//2, WindowParams.HEIGHT- 150)
                )
            }
        if number_level == 2:
            enemies_by_room = {
                9: pygame.sprite.Group(
                    RangeEnemy(100, WindowParams.HEIGHT-150),
                    RangeEnemy(100, 100),
                    MeleeEnemy(WindowParams.WIDTH//2, 90)
                ),
                11: pygame.sprite.Group(
                    RangeEnemy(100, 100),
                    MeleeEnemy(WindowParams.WIDTH -150, 150),
                    MeleeEnemy(WindowParams.WIDTH - 150, WindowParams.HEIGHT-160)
                ),
                3: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH - 120, 100),
                    MeleeEnemy(100, WindowParams.HEIGHT - 120)
                ),
                12: pygame.sprite.Group(
                    RangeEnemy(200, WindowParams.HEIGHT - 120),
                    MeleeEnemy(WindowParams.WIDTH-150, WindowParams.HEIGHT - 120)
                )
            }
        if number_level == 3:
            enemies_by_room = {
                9: pygame.sprite.Group(
                    RangeEnemy(WindowParams.WIDTH - 200, 120),
                    RangeEnemy(WindowParams.WIDTH//2, 120),
                    MeleeEnemy(WindowParams.WIDTH -120, WindowParams.HEIGHT//2)
                ),
                11: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH - 200, 120),
                    MeleeEnemy(WindowParams.WIDTH - 140, WindowParams.HEIGHT - 140)
                ),
                5: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH //2,  WindowParams.HEIGHT//2)
                ),
                12: pygame.sprite.Group(
                    RangeEnemy(100, WindowParams.HEIGHT//2),
                    MeleeEnemy(WindowParams.WIDTH//2, WindowParams.HEIGHT - 125)
                ),
                13: pygame.sprite.Group(
                    RangeEnemy(WindowParams.WIDTH//2 + 200, 120),
                    MeleeEnemy(120, 120),
                    MeleeEnemy(WindowParams.WIDTH-125, WindowParams.HEIGHT-125)
                )
            }
        if number_level == 4:
            enemies_by_room = {4: pygame.sprite.Group(
                RangeBossEnemy(WindowParams.WIDTH//2, WindowParams.HEIGHT//2)
            )}
        return enemies_by_room


class GetEnemiesStructure(pygame.sprite.Sprite):

    ENEMIES: Dict[int, pygame.sprite.Group] = EnemiesStructure.get_enemies_on_level(Rooms.NUMBER_LEVEL)

    @staticmethod
    def update_level():
        GetEnemiesStructure.ENEMIES = EnemiesStructure.get_enemies_on_level(Rooms.NUMBER_LEVEL)

    @staticmethod
    def restart_game():
        GetEnemiesStructure.ENEMIES = EnemiesStructure.get_enemies_on_level(Rooms.NUMBER_LEVEL)
