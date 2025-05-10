import pygame
import random
from typing import Dict
from objects.interface_objects import Barrel, Column, Coin
from structures_and_parameters.parameters_game import WindowParams


def get_structures(number_level: int) -> Dict[int, pygame.sprite.Group]:
    if number_level == 1:
        structures_by_room = {0: {"barrels": pygame.sprite.Group(
            Barrel(77, 77),
            Barrel(145, 77),
            Barrel(77, 145),
            Barrel(213, 77),
            Barrel(WindowParams.WIDTH - 232, WindowParams.HEIGHT - 77),
        ),
            "coins": pygame.sprite.Group(
                Coin(WindowParams.WIDTH // 2 + 300, WindowParams.HEIGHT // 2)
            ),
            "columns": pygame.sprite.Group(
                Column(WindowParams.WIDTH - 300, WindowParams.HEIGHT - 77, random.randint(1, 6)),
                Column(WindowParams.WIDTH - 300, WindowParams.HEIGHT - 145, random.randint(1, 6)),
                Column(WindowParams.WIDTH // 2 - 200, WindowParams.HEIGHT // 2, random.randint(1, 6)),
                Column(WindowParams.WIDTH // 2 - 140, WindowParams.HEIGHT // 2 + 72, random.randint(1, 6)),
            ),
            "potions": pygame.sprite.Group(
            )
        }
            ,
            8: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH // 2 - 200, WindowParams.HEIGHT // 2 - 68),
                Barrel(WindowParams.WIDTH - 77, WindowParams.HEIGHT // 2),
                Barrel(WindowParams.WIDTH - 145, WindowParams.HEIGHT // 2 + 145),
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH // 2 - 200, WindowParams.HEIGHT // 2, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 132, WindowParams.HEIGHT // 2 - 72, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 72, WindowParams.HEIGHT // 2 + 72, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 145, WindowParams.HEIGHT // 2 + 72, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 218, WindowParams.HEIGHT // 2 + 144, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            1: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH // 2 - 68, WindowParams.HEIGHT // 2 + 68),
                Barrel(WindowParams.WIDTH // 2 + 68, WindowParams.HEIGHT // 2)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 72, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 72, WindowParams.HEIGHT // 2 - 72, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            2: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH // 2 - 200, WindowParams.HEIGHT // 2 + 68),
                Barrel(WindowParams.WIDTH // 2 - 132, WindowParams.HEIGHT // 2)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH - 77, WindowParams.HEIGHT // 2 - 77, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 145, WindowParams.HEIGHT // 2 - 77, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 222, WindowParams.HEIGHT // 2, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 222, WindowParams.HEIGHT // 2 + 72, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 200, WindowParams.HEIGHT // 2, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            12: {"barrels": pygame.sprite.Group(
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH // 2 - 300, 77, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 300, 145, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 373, 145, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 77, WindowParams.HEIGHT // 2 + 145, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 150, WindowParams.HEIGHT // 2 + 145, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 210, WindowParams.HEIGHT // 2 + 73, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            11: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2),
                Barrel(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 + 68),
                Barrel(WindowParams.WIDTH // 2 - 68, WindowParams.HEIGHT // 2)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 73, random.randint(1, 6)),
                ),
                "potions": pygame.sprite.Group(
                )
            },
            7: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2),
                Barrel(WindowParams.WIDTH // 2 - 68, WindowParams.HEIGHT // 2 + 68),
                Barrel(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 68),
                Barrel(WindowParams.WIDTH // 2 + 68, WindowParams.HEIGHT // 2),
                Barrel(WindowParams.WIDTH // 2 + 68, WindowParams.HEIGHT // 2 + 68),
                Barrel(WindowParams.WIDTH // 2 + 120, WindowParams.HEIGHT // 2 - 50)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                ),
                "potions": pygame.sprite.Group(
                )
            }
        }
    if number_level == 2:
        structures_by_room = {
            0: {"barrels": pygame.sprite.Group(
                Barrel(222, 222),
                Barrel(WindowParams.WIDTH -222, WindowParams.HEIGHT -222)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(77, WindowParams.HEIGHT-145,random.randint(1, 6)),
                    Column(143, WindowParams.HEIGHT - 145, random.randint(1, 6)),
                    Column(215, WindowParams.HEIGHT - 77, random.randint(1, 6)),
                    Column(WindowParams.WIDTH-148, 80, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 148, 148, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 77, 218, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            3: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH//2, WindowParams.HEIGHT//2)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH//2 + 116, 79, random.randint(1, 6)),
                    Column(WindowParams.WIDTH//2 + 116, 147, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 + 45, 218, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 116, WindowParams.HEIGHT-79, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 116, WindowParams.HEIGHT-147, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 - 45, WindowParams.HEIGHT-218, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            9: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH//2, WindowParams.HEIGHT//2),
                Barrel(WindowParams.WIDTH // 2+70, WindowParams.HEIGHT // 2),
                Barrel(WindowParams.WIDTH // 2-55, WindowParams.HEIGHT // 2+55)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(WindowParams.WIDTH // 2, WindowParams.HEIGHT//2-72, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2, WindowParams.HEIGHT // 2 - 145, random.randint(1, 6)),
                    Column(WindowParams.WIDTH // 2 + 70, WindowParams.HEIGHT // 2 + 72, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            11: {"barrels": pygame.sprite.Group(
                Barrel(WindowParams.WIDTH-77, WindowParams.HEIGHT-295),
                Barrel(WindowParams.WIDTH - 145, WindowParams.HEIGHT - 295),
                Barrel(WindowParams.WIDTH - 212, WindowParams.HEIGHT - 295)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(222, 80, random.randint(1, 6)),
                    Column(222, 148, random.randint(1, 6)),
                    Column(294, 148, random.randint(1, 6)),
                    Column(WindowParams.WIDTH-282, WindowParams.HEIGHT-295, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 282, WindowParams.HEIGHT - 224, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 282, WindowParams.HEIGHT - 150, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 282, WindowParams.HEIGHT - 78, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            },
            12: {"barrels": pygame.sprite.Group(
                Barrel(290, WindowParams.HEIGHT - 220),
                Barrel(290, WindowParams.HEIGHT - 290),
                Barrel(WindowParams.WIDTH-80, 80),
                Barrel(WindowParams.WIDTH - 80, 150),
                Barrel(WindowParams.WIDTH - 150, 80),
                Barrel(WindowParams.WIDTH - 220, 80)
            ),
                "coins": pygame.sprite.Group(
                ),
                "columns": pygame.sprite.Group(
                    Column(80, WindowParams.HEIGHT-80, random.randint(1, 6)),
                    Column(150, WindowParams.HEIGHT-150, random.randint(1, 6)),
                    Column(220, WindowParams.HEIGHT-220, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 80, WindowParams.HEIGHT//2 +120, random.randint(1, 6)),
                    Column(WindowParams.WIDTH - 150, WindowParams.HEIGHT // 2 + 120, random.randint(1, 6))
                ),
                "potions": pygame.sprite.Group(
                )
            }
        }
    return structures_by_room