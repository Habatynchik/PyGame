import pygame
import random

class Fireball:
    def __init__(self, size, display_surface):
        self.SCREEN_WIDTH = display_surface.get_rect().width
        self.SCREEN_HEIGHT = display_surface.get_rect().height
        self.damage = self.SCREEN_WIDTH / 100
        self.size = size
        self.surface = pygame.image.load('./images/Fireball/Fireball_1.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, size)
        self.rect = self.surface.get_rect()
        self.rotated = self.surface
        self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
        self.speed = random.randint(150, 600)
        self.rect.left = random.randint(0, self.SCREEN_WIDTH)
        self.rotation = 0

    def update(self, delta_time):
        self.rect.center += self.direction * delta_time * self.speed
        self.rotated = pygame.transform.rotozoom(self.surface, self.rotation, random.uniform(0.9, 1.1))
        self.rotation += 60 * delta_time
        self.rect = self.rotated.get_rect(center=self.rect.center)
        if self.rect.bottom > self.SCREEN_HEIGHT:
            self.rect.top = 0
            self.speed = random.randint(150, 400)
            self.direction = pygame.Vector2(random.uniform(-0.5, 0.5), 1)
            self.rect.left = random.randint(0, self.SCREEN_WIDTH)

    def explosion(self):
        self.surface = pygame.image.load('./images/Fireball/explosion.gif').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, self.size)
        self.speed = 0