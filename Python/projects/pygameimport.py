import pygame

# 1. Инициализация и создание окна
pygame.init()
width, height = 400, 400
screen = pygame.display.set_mode((width, height)) # Исправлено: set_mode вместо set_screen
pygame.display.set_caption("Пиксели в Pygame")

# 2. Создаем массив пикселей экрана
pixel_array = pygame.PixelArray(screen)

# 3. Красим пиксели [x, y] = (R, G, B)
for x in range(width):
    for y in range(height):
        # Рисуем градиент
        r = int(x / width * 255)
        g = int(y / height * 255)
        pixel_array[x, y] = (r, g, 100)

# 4. Закрываем массив пикселей, чтобы Pygame мог отобразить их на экране
pixel_array.close()

# 5. Главный цикл программы (удерживает окно открытым)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Обновляем содержимое экрана каждый кадр
    pygame.display.flip()

pygame.quit()
