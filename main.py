import pygame
from player import Player

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(3, display_surface)

fireball_surface = pygame.image.load('./images/Fireball/Fireball_1.png').convert_alpha()
fireball_surface = pygame.transform.scale(fireball_surface, (30, 30))

game_is_running = True

while game_is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False

    keys = pygame.key.get_pressed()
    player.move(keys)

    display_surface.fill((255, 40, 210))
    display_surface.blit(player.surface, player.rect)
    display_surface.blit(fireball_surface, (100, 100))
    pygame.display.update()

pygame.init()