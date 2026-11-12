import pygame 
import func
from time import sleep as sl
# A = [[0 for _ in range(9)] for _ in range(9)]

pygame.init()
pygame.font.init()

A = [
  [5, 3, 0, 0, 7, 0, 0, 0, 0],
  [6, 0, 0, 1, 9, 5, 0, 0, 0],
  [0, 9, 8, 0, 0, 0, 0, 6, 0],
  [8, 0, 0, 0, 6, 0, 0, 0, 3],
  [4, 0, 0, 8, 0, 3, 0, 0, 1],
  [7, 0, 0, 0, 2, 0, 0, 0, 6],
  [0, 6, 0, 0, 0, 0, 2, 8, 0],
  [0, 0, 0, 4, 1, 9, 0, 0, 5],
  [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Test 1")

font = pygame.font.SysFont("arial", 40)

cell_size = 50
start_x = (width - (cell_size * 9)) // 2
start_y = (height - (cell_size * 9)) // 2

running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(WHITE)

  for i in range(10):
    thickness = 4 if i % 3 == 0 else 1
    pygame.draw.line(screen, BLACK, (start_x, start_y + i * cell_size), (start_x + 9 * cell_size, start_y + i * cell_size), thickness)
    pygame.draw.line(screen, BLACK, (start_x + i * cell_size, start_y), (start_x + i * cell_size, start_y + 9 * cell_size), thickness)

  for r in range(9):
    for c in range(9):
      if A[r][c] != 0:
        text_surface = font.render(str(A[r][c]), True, BLUE)
        text_rect = text_surface.get_rect(center=(start_x + c * cell_size + cell_size // 2, start_y + r * cell_size + cell_size // 2))
        screen.blit(text_surface, text_rect)
  func.f(A)
  sl(1)
  pygame.display.flip()

pygame.quit()
print(A)