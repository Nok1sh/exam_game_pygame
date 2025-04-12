import pygame
from parameters_game import WindowParams, Color, Rooms
from groups_objects import player_group, walls_group


screen = pygame.display.set_mode(
    (WindowParams.WIDTH, WindowParams.HEIGHT),
    pygame.RESIZABLE
)

pygame.display.set_caption('game window')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(Color.BLACK)
    player_group.update(walls_group(Rooms.ROOM))
    player_group.draw(screen)
    walls_group(Rooms.ROOM).draw(screen)
    pygame.display.flip()
    clock.tick(WindowParams.FPS)
