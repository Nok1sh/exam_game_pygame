import pygame
from objects.world_objects.world_structures import Walls
from structures_and_parameters.parameters_game import WindowParams, Textures


def room_number(number: int) -> pygame.sprite.Group:
    group_of_walls = pygame.sprite.Group()
    move_horizontal: int = 5
    move_vertical: int = 5
    if number == 0:  # room with 2 doors on vertical walls
        group_of_walls.add(
            Walls(0-move_horizontal, 0-move_vertical, WindowParams.WIDTH + 2*move_horizontal, 50, Textures.WALL),
            Walls(0-move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH + 2*move_horizontal, 50, Textures.WALL),

            Walls(0-move_horizontal, 50-move_vertical, 50, WindowParams.HEIGHT//2 - 75, Textures.WALL),
            Walls(0-move_horizontal, 75 + WindowParams.HEIGHT//2, 50, WindowParams.HEIGHT//2, Textures.WALL),

            Walls(WindowParams.WIDTH-50 + move_horizontal, 50-move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH-50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 1:  # room with 4 doors on all walls
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0-move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(0 - move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 2:  # room with 3 doors/ one on right vertical wall and two on horizontal walls
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT - 50 + move_vertical,
                  WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50,
                  WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 3:  # room with 2 doors on horizontal doors
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT - 50 + move_vertical,
                  WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL)
        )
    elif number == 4:  # room with 1 door on lower horizontal wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT - 50 + move_vertical,
                  WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL)
        )
    elif number == 5:  # room with 1 door on upper horizontal wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL)
        )
    elif number == 6:  # room with 1 door on right vertical wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50,
                  WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 7:  # room with 1 door on left vertical wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(0 - move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL)
        )
    elif number == 8:  # room with 2 doors on left and top wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0-move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(0 - move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL)
        )
    elif number == 9:  # room with 2 doors/ one on right vertical wall and one on lower horizontal wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT - 50 + move_vertical,
                  WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50,
                  WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 10:  # room with 3 doors/ two on vertical walls and one on lower horizontal wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(0 - move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 11:  # room with 2 doors/ one on left vertical wall and one on lower horizontal wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, WindowParams.HEIGHT-50 + move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(0 - move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL)
        )
    elif number == 12:  # room with 2 doors on right and top wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0-move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL)
        )
    elif number == 13:  # room with 3 doors/ two on vertical walls and one on upper horizontal wall
        group_of_walls.add(
            Walls(0 - move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2 - 75, 50, Textures.WALL),
            Walls(75 + WindowParams.WIDTH // 2 + move_horizontal, 0 - move_vertical, WindowParams.WIDTH // 2, 50, Textures.WALL),

            Walls(0 - move_horizontal, WindowParams.HEIGHT - 50 + move_vertical, WindowParams.WIDTH + move_horizontal, 50, Textures.WALL),

            Walls(0 - move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(0 - move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL),

            Walls(WindowParams.WIDTH - 50 + move_horizontal, 50 - move_vertical, 50, WindowParams.HEIGHT // 2 - 75, Textures.WALL),
            Walls(WindowParams.WIDTH - 50 + move_horizontal, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2, Textures.WALL)
        )
    return group_of_walls
