import pygame
import math
import time

# Инициализация pygame
pygame.init()

# Настройки экрана
WIDTH, HEIGHT = 400, 400
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 150  # Радиус циферблата
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Аналоговые часы")

# Цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Таймер
clock = pygame.time.Clock()

def draw_hand(angle, length, color, width=4):
    """ Функция рисует стрелку по заданному углу и длине """
    end_x = CENTER[0] + length * math.cos(math.radians(angle))
    end_y = CENTER[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(screen, color, CENTER, (end_x, end_y), width)

def draw_clock():
    """ Функция рисует круглый циферблат и стрелки часов """
    screen.fill(BLACK)
    pygame.draw.circle(screen, WHITE, CENTER, RADIUS, 4)  # Циферблат

    # Отметки часов (1-12)
    for i in range(12):
        angle = math.radians(i * 30)  # 360° / 12 = 30°
        mark_x = CENTER[0] + (RADIUS - 10) * math.cos(angle)
        mark_y = CENTER[1] - (RADIUS - 10) * math.sin(angle)
        pygame.draw.circle(screen, WHITE, (int(mark_x), int(mark_y)), 4)

    # Получаем текущее время
    t = time.localtime()
    hours = t.tm_hour % 12
    minutes = t.tm_min
    seconds = t.tm_sec

    # Углы для стрелок
    sec_angle = 90 - (seconds * 6)      # 360° / 60 = 6° на секунду
    min_angle = 90 - (minutes * 6)      # 360° / 60 = 6° на минуту
    hour_angle = 90 - (hours * 30 + minutes * 0.5)  # 360° / 12 = 30° на час

    # Рисуем стрелки
    draw_hand(hour_angle, RADIUS * 0.5, BLUE, 6)   # Часовая стрелка
    draw_hand(min_angle, RADIUS * 0.75, GREEN, 4)  # Минутная стрелка
    draw_hand(sec_angle, RADIUS * 0.9, RED, 2)     # Секундная стрелка

running = True
while running:
    draw_clock()
    pygame.display.flip()  # Обновление экрана

    # Проверка выхода
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(1)  # Обновление каждую секунду

pygame.quit()