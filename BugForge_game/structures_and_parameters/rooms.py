import pygame
from objects.world_objects.world_structures import Walls
from structures_and_parameters.parameters_game import WindowParams, Textures


class WallOfRooms:
    MOVE_HORIZONTAL: int = 5
    MOVE_VERTICAL: int = 5

    TOP_WALL: Walls = Walls(0-MOVE_HORIZONTAL, 0-MOVE_VERTICAL, WindowParams.WIDTH + 2*MOVE_HORIZONTAL, 50)
    TOP_FIRST_HALF_WALL: Walls = Walls(0 - MOVE_HORIZONTAL, 0 - MOVE_VERTICAL, WindowParams.WIDTH // 2 - 75, 50)
    TOP_SECOND_HALF_WALL: Walls = Walls(75 + WindowParams.WIDTH // 2 + MOVE_HORIZONTAL, 0-MOVE_VERTICAL, WindowParams.WIDTH // 2, 50)
    BOTTOM_WALL: Walls = Walls(0-MOVE_HORIZONTAL, WindowParams.HEIGHT-50 + MOVE_VERTICAL, WindowParams.WIDTH + 2*MOVE_HORIZONTAL, 50)
    BOTTOM_FIRST_HALF_WALL: Walls = Walls(0 - MOVE_HORIZONTAL, WindowParams.HEIGHT-50 + MOVE_VERTICAL, WindowParams.WIDTH // 2 - 75, 50)
    BOTTOM_SECOND_HALF_WALL: Walls = Walls(75 + WindowParams.WIDTH // 2 + MOVE_HORIZONTAL, WindowParams.HEIGHT-50 + MOVE_VERTICAL, WindowParams.WIDTH // 2, 50),
    LEFT_WALL: Walls = Walls(0 - MOVE_HORIZONTAL, 50 - MOVE_VERTICAL, 50, WindowParams.HEIGHT)
    LEFT_FIRST_HALF_WALL: Walls = Walls(0-MOVE_HORIZONTAL, 50-MOVE_VERTICAL, 50, WindowParams.HEIGHT//2 - 75)
    LEFT_SECOND_HALF_WALL: Walls = Walls(0-MOVE_HORIZONTAL, 75 + WindowParams.HEIGHT//2, 50, WindowParams.HEIGHT//2)
    RIGHT_WALL: Walls = Walls(WindowParams.WIDTH - 50 + MOVE_HORIZONTAL, 50 - MOVE_VERTICAL, 50, WindowParams.HEIGHT)
    RIGHT_FIRST_HALF_WALL: Walls = Walls(WindowParams.WIDTH-50 + MOVE_HORIZONTAL, 50-MOVE_VERTICAL, 50, WindowParams.HEIGHT // 2 - 75)
    RIGHT_SECOND_HALF_WALL: Walls = Walls(WindowParams.WIDTH-50 + MOVE_HORIZONTAL, 75 + WindowParams.HEIGHT // 2, 50, WindowParams.HEIGHT // 2)


def room_number(number: int) -> pygame.sprite.Group:
    group_of_walls = pygame.sprite.Group()
    move_horizontal: int = 5
    move_vertical: int = 5
    if number == 0:  # room with 2 doors on vertical walls
        group_of_walls.add(
            WallOfRooms.TOP_WALL,
            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 1:  # room with 4 doors on all walls
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 2:  # room with 3 doors/ one on right vertical wall and two on horizontal walls
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 3:  # room with 2 doors on horizontal doors
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_WALL
        )
    elif number == 4:  # room with 1 door on lower horizontal wall
        group_of_walls.add(
            WallOfRooms.TOP_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_WALL
        )
    elif number == 5:  # room with 1 door on upper horizontal wall
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_WALL
        )
    elif number == 6:  # room with 1 door on right vertical wall
        group_of_walls.add(
            WallOfRooms.TOP_WALL,

            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 7:  # room with 1 door on left vertical wall
        group_of_walls.add(
            WallOfRooms.TOP_WALL,

            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_WALL
        )
    elif number == 8:  # room with 2 doors on left and top wall
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_WALL
        )
    elif number == 9:  # room with 2 doors/ one on right vertical wall and one on lower horizontal wall
        group_of_walls.add(
            WallOfRooms.TOP_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 10:  # room with 3 doors/ two on vertical walls and one on lower horizontal wall
        group_of_walls.add(
            WallOfRooms.TOP_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 11:  # room with 2 doors/ one on left vertical wall and one on lower horizontal wall
        group_of_walls.add(
            WallOfRooms.TOP_WALL,

            WallOfRooms.BOTTOM_FIRST_HALF_WALL,
            WallOfRooms.BOTTOM_SECOND_HALF_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_WALL
        )
    elif number == 12:  # room with 2 doors on right and top wall
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    elif number == 13:  # room with 3 doors/ two on vertical walls and one on upper horizontal wall
        group_of_walls.add(
            WallOfRooms.TOP_FIRST_HALF_WALL,
            WallOfRooms.TOP_SECOND_HALF_WALL,

            WallOfRooms.BOTTOM_WALL,

            WallOfRooms.LEFT_FIRST_HALF_WALL,
            WallOfRooms.LEFT_SECOND_HALF_WALL,

            WallOfRooms.RIGHT_FIRST_HALF_WALL,
            WallOfRooms.RIGHT_SECOND_HALF_WALL
        )
    return group_of_walls
