import pygame
import random

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
fps = 60
clock = pygame.time.Clock()


def game_over():
    font = pygame.font.Font(None, 50)
    text = font.render("Game over!", True, pygame.Color('yellow'))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    screen.blit(text, (text_x, text_y))
    waiting = True
    while waiting:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False
        pygame.display.flip()


