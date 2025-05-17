import pygame
from typing import Dict
from structures_and_parameters.parameters_game import WindowParams
from structures_and_parameters.structures_on_each_level import Rooms
from objects.action_objects import MeleeEnemy, RangeEnemy, RangeBossEnemy


class EnemiesStructure(pygame.sprite.Sprite):
    @staticmethod
    def get_enemies_on_level(number_level: int) -> Dict[int, pygame.sprite.Group]:
        if number_level == 1:
            enemies_by_room = {1: pygame.sprite.Group(
                RangeEnemy(100, 100),
                MeleeEnemy(WindowParams.WIDTH//2 - 200, WindowParams.HEIGHT - 100)
            ),
                2: pygame.sprite.Group(
                    MeleeEnemy(200, WindowParams.HEIGHT//2-200)
                ),
                8: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH - 100, 100),
                    MeleeEnemy(WindowParams.WIDTH - 100, WindowParams.HEIGHT - 100)
                ),
                12: pygame.sprite.Group(
                    RangeEnemy(100, WindowParams.HEIGHT-100),
                    RangeEnemy(WindowParams.WIDTH//2, WindowParams.HEIGHT- 100)
                )
            }
        if number_level == 2:
            enemies_by_room = {
                9: pygame.sprite.Group(
                    RangeEnemy(100, WindowParams.HEIGHT-100),
                    RangeEnemy(100, 100),
                    MeleeEnemy(WindowParams.WIDTH//2, 70)
                ),
                11: pygame.sprite.Group(
                    RangeEnemy(100, 100),
                    MeleeEnemy(WindowParams.WIDTH -100, 100),
                    MeleeEnemy(WindowParams.WIDTH - 100, WindowParams.HEIGHT-100)
                ),
                3: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH - 100, 100),
                    MeleeEnemy(100, WindowParams.HEIGHT - 100)
                ),
                12: pygame.sprite.Group(
                    RangeEnemy(200, 70),
                    MeleeEnemy(WindowParams.WIDTH-150, WindowParams.HEIGHT - 100)
                )
            }
        if number_level == 3:
            enemies_by_room = {
                9: pygame.sprite.Group(
                    RangeEnemy(WindowParams.WIDTH - 200, 100),
                    RangeEnemy(WindowParams.WIDTH//2, 100),
                    MeleeEnemy(WindowParams.WIDTH -100, WindowParams.HEIGHT//2)
                ),
                11: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH - 200, 100),
                    MeleeEnemy(WindowParams.WIDTH - 100, WindowParams.HEIGHT - 100)
                ),
                5: pygame.sprite.Group(
                    MeleeEnemy(WindowParams.WIDTH //2,  WindowParams.HEIGHT//2)
                ),
                12: pygame.sprite.Group(
                    RangeEnemy(100, WindowParams.HEIGHT//2),
                    MeleeEnemy(WindowParams.WIDTH//2, WindowParams.HEIGHT - 100)
                ),
                13: pygame.sprite.Group(
                    RangeEnemy(WindowParams.WIDTH//2 + 200, 100),
                    MeleeEnemy(100, 100),
                    MeleeEnemy(WindowParams.WIDTH-100, WindowParams.HEIGHT-100)
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