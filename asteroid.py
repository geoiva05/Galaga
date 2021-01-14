import pygame
import sys
import random
import os
from load_image import load_image

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)


class asteroid(pygame.sprite.Sprite):
    image = load_image(random.choice(["asteroid_1.png", "asteroid_2.png"]), colorkey=-1)

    def __init__(self, *group):
        super().__init__(*group)
        self.image = pygame.transform.scale(asteroid.image, (40, 34))
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(800 - self.rect.width)
        self.rect.y = random.randrange(0, 34)
        self.speedy = random.randrange(1, 6)
        self.speedx = random.randrange(-3, 3)

    def update(self):
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if self.rect.top > 600 + 10 or self.rect.left < -25 or self.rect.right > 800 + 20:
            self.kill()