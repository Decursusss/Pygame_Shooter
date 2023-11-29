import sys
import pygame
import random

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Pygame")

rect_width, rect_height = 100, 200
rect_x, rect_y = (screen_width / 2) - (rect_width / 2) , (screen_height / 2) - (rect_height / 2)

STEP = 10

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_UP and rect_y >= STEP:
                rect_y -= STEP
            if event.key == pygame.K_DOWN and rect_y <= screen_height - rect_height - STEP:
                rect_y += STEP
            if event.key == pygame.K_LEFT and rect_x >= STEP:
                rect_x -= STEP
            if event.key == pygame.K_RIGHT and rect_x <= screen_width - rect_width - STEP:
                rect_x += STEP


    screen.fill((32, 52, 71))
    pygame.draw.rect(screen, pygame.Color('lightyellow'), (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()
