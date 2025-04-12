import pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Переход между комнатами")

# Цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Игрок (квадрат)
player = pygame.Rect(400, 300, 30, 30)
player_speed = 5

# Комнаты (просто разные фоны и названия)
current_room = 1  # Начинаем в комнате 1

# Игровой цикл
running = True
clock = pygame.time.Clock()

while running:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление игроком
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # Проверка выхода за границы экрана
    if player.left < 0:  # Выход влево
        current_room = 2  # Переход в комнату 2
        player.right = WIDTH - 1  # Появляемся справа
    elif player.right > WIDTH:  # Выход вправо
        current_room = 1  # Переход в комнату 1
        player.left = 1  # Появляемся слева
    elif player.top < 0:  # Выход вверх
        current_room = 3  # Переход в комнату 3
        player.bottom = HEIGHT - 1  # Появляемся снизу
    elif player.bottom > HEIGHT:  # Выход вниз
        current_room = 4  # Переход в комнату 4
        player.top = 1  # Появляемся сверху

    # Отрисовка
    if current_room == 1:
        screen.fill(RED)  # Комната 1 — красная
        room_text = "Комната 1 (Выход →)"
    elif current_room == 2:
        screen.fill(GREEN)  # Комната 2 — зелёная
        room_text = "Комната 2 (Выход ←)"
    elif current_room == 3:
        screen.fill(BLUE)  # Комната 3 — синяя
        room_text = "Комната 3 (Выход ↓)"
    elif current_room == 4:
        screen.fill(BLACK)  # Комната 4 — чёрная
        room_text = "Комната 4 (Выход ↑)"

    # Рисуем игрока
    pygame.draw.rect(screen, WHITE, player)

    # Выводим название комнаты
    font = pygame.font.SysFont(None, 36)
    text = font.render(room_text, True, WHITE)
    screen.blit(text, (20, 20))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()