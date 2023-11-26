import time
import pygame
import sys
from SquareM1 import Square1
from SquareM2 import Square2

def CountSpeeds(m1, m2, v1, v2):
    vv1 = v1
    vv2 = v2
    v2 = (2 * m1 * v1 + m2 * v2 - m1 * v2) / (m1 + m2)
    v1 = v2 + vv2 - vv1
    v1 = round(v1, 9)
    v2 = round(v2, 9)
    return v1, v2

square1x = 300
square1y = 563

square2x = 470
square2y = 527

count = 0
speed1 = 0
speed2 = -10
weight1 = 1
weight2 = 1000000

pygame.init()
screen = pygame.display.set_mode((1500, 700))
pygame.display.set_caption('Квадратики')

bg_color = (255, 255, 255)
surf_color = (80, 205, 150)
text_color = (0, 0, 0)

square1 = Square1(screen)
square2 = Square2(screen)
square1_rect = square1.image.get_rect()
square2_rect = square2.image.get_rect()

surf_left = pygame.Surface((100, 700))
surf_bottom = pygame.Surface((1500, 200))
surf_left.fill(surf_color)
surf_bottom.fill(surf_color)
screen_rect = screen.get_rect()
surf_left_rect = surf_left.get_rect()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

while True:
    text_surface = my_font.render(str(count), False, (0, 0, 0))
    screen.fill(bg_color)
    screen.blit(surf_bottom, (0, 600))
    screen.blit(surf_left, (0, 0))
    square2x += speed2
    square2_rect.x = square2x
    if square2_rect.left < square1_rect.right:
        square2_rect.left = square1_rect.right
        square2x = square2_rect.x
    square1x += speed1
    square1_rect.x = square1x
    if square1_rect.left < surf_left_rect.right:
        square1_rect.left = surf_left_rect.right
        square1x = square1_rect.x
    if square1_rect.right > square2_rect.left:
        square1_rect.right = square2_rect.left
        square1x = square1_rect.x
    if square1_rect.left == surf_left_rect.right and square2_rect.left > screen_rect.right:
        square2_rect.left = square1_rect.right + 100
        square2x = square2_rect.x
    square1_rect.y = square1y
    square2_rect.y = square2y
    square1.output(square1_rect.x, square1_rect.y)
    square2.output(square2_rect.x, square2_rect.y)
    screen.blit(text_surface, (700, 0))
    if square2_rect.left <= surf_left_rect.left + (square1_rect.right - square1_rect.left):
        square2_rect.left = square1_rect.right + 0.001
        square2x = square2_rect.x
    if square1_rect.right >= square2_rect.left:
        count += 1
        square1_rect.right = square2_rect.left - 0.001
        square1x = square1_rect.x
        speed1, speed2 = CountSpeeds(weight1, weight2, speed1, speed2)
        speed1 = round(speed1, 9)
        speed2 = round(speed2, 9)
    if square1_rect.left <= surf_left_rect.right:
        count += 1
        square1_rect.left = surf_left_rect.right + 0.001
        square1x = square1_rect.x
        speed1 *= -1
    if square2_rect.left > screen_rect.right and speed1 > 0 and speed2 > 0 and speed2 > speed1:
        time.sleep(2)
        print('================TOTAL================')
        print('                ' + str(count) + '                ')
        print('=====================================')
        sys.exit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.time.delay(12)
    pygame.display.update()
