import pygame
from parameters_game import WindowParams, Color, Rooms, ActionParams
from groups_objects import player_group, walls_group, add_magic_ball, magic_balls, bars, projectiles, enemies_by_room
pygame.init()

player = next(iter(player_group))
#Floor.floor(screen)


def main_game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (pygame.time.get_ticks() - ActionParams.DELAY_MAGIC_BALLS >= ActionParams.LAST_MAGIC_BALLS) and player.mana_pool > 0:
                        add_magic_ball(player.line_move, player.rect.x, player.rect.y)
                        player.mana_pool -= 1
                        ActionParams.LAST_MAGIC_BALLS = pygame.time.get_ticks()

        WindowParams.SCREEN.fill(Color.BLACK)
        #Floor.floor(screen)
        walls_room = walls_group(Rooms.ROOM)
        current_enemies = enemies_by_room.get(Rooms.ROOM)
        if current_enemies:
            current_enemies.update(player, walls_room, magic_balls, projectiles)
            current_enemies.draw(WindowParams.SCREEN)
        projectiles.update(player, walls_room)
        magic_balls.update(walls_room)
        player_group.update(walls_room)
        bars.update()
        projectiles.draw(WindowParams.SCREEN)
        player_group.draw(WindowParams.SCREEN)
        magic_balls.draw(WindowParams.SCREEN)
        walls_group(Rooms.ROOM).draw(WindowParams.SCREEN)
        bars.draw(WindowParams.SCREEN)
        pygame.display.flip()
        WindowParams.CLOCK.tick(WindowParams.FPS)
