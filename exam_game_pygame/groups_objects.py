import pygame
from objects_ import Player, Walls
from parameters_game import WindowParams

player_group = pygame.sprite.Group(
    Player()
)

def room_number(number: int):
    if number == 0:  # room with 2 doors on vertical walls
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH, 50),
            Walls(0, WindowParams.HEIGHT-50, WindowParams.WIDTH, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT//2 - 100),
            Walls(0, 100 + WindowParams.HEIGHT//2, 50, WindowParams.HEIGHT//2),

            Walls(WindowParams.WIDTH-50, 50, 50, WindowParams.HEIGHT // 2 - 100),
            Walls(WindowParams.WIDTH-50, 100 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2)
        )

    elif number == 1:  # room with 4 doors on all walls
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, 0, WindowParams.WIDTH // 2, 50),

            Walls(0, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT // 2 - 100),
            Walls(0, 100 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT // 2 - 100),
            Walls(WindowParams.WIDTH - 50, 100 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2)
        )
    elif number == 2:  # room with 3 doors/ one on right vertical wall and two on horizontal walls
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, 0, WindowParams.WIDTH // 2, 50),

            Walls(0, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT // 2 - 100),
            Walls(WindowParams.WIDTH - 50, 100 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2)
        )
    elif number == 3:  # room with 2 doors on horizontal doors
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, 0, WindowParams.WIDTH // 2, 50),

            Walls(0, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT)
        )
    elif number == 4:  # room with 1 door on lower horizontal wall
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH, 50),

            Walls(0, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, WindowParams.HEIGHT-50, WindowParams.WIDTH // 2, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT)
        )
    elif number == 5:  # room with 1 door on upper horizontal wall
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH // 2 - 100, 50),
            Walls(100 + WindowParams.WIDTH // 2, 0, WindowParams.WIDTH // 2, 50),

            Walls(0, WindowParams.HEIGHT - 50, WindowParams.WIDTH, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT)
        )
    elif number == 6:  # room with 1 door on right vertical wall
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH, 50),

            Walls(0, WindowParams.HEIGHT - 50, WindowParams.WIDTH, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT // 2 - 100),
            Walls(WindowParams.WIDTH - 50, 100 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2)
        )
    elif number == 7:  # room with 1 door on left vertical wall
        group_of_walls = pygame.sprite.Group(
            Walls(0, 0, WindowParams.WIDTH, 50),

            Walls(0, WindowParams.HEIGHT - 50, WindowParams.WIDTH, 50),

            Walls(0, 50, 50, WindowParams.HEIGHT // 2 - 100),
            Walls(0, 100 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2),

            Walls(WindowParams.WIDTH - 50, 50, 50, WindowParams.HEIGHT)
        )

    return group_of_walls

def walls_group(number: int):
    walls = room_number(number)
    return walls



