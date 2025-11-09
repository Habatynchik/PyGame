import random
import pygame
from fireball import Fireball
from player import Player

def display_score():
    ticks = pygame.time.get_ticks() // 100
    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(f"Score: {ticks}", True, (0, 0, 0))
    score_rect = score_text.get_rect(center=(SCREEN_WIDTH / 2, 10))
    return score_text, score_rect

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
player = Player(400, display_surface)
fireballs = []
for i in range(13):
    size = random.randint(50, 100)
    fireballs.append(Fireball((size, size), display_surface))

game_is_running = True
clock = pygame.time.Clock()

while game_is_running:
    display_surface.fill((255, 40, 210))
    delta_time = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_is_running = False
    keys = pygame.key.get_pressed()

    player.move(keys, delta_time)

    for fireball in fireballs:
        fireball.update(delta_time)
        display_surface.blit(fireball.rotated, fireball.rect)
        if player.check_collision(fireball):
            player.receive_damage(fireball)
            fireball.explosion()

    player.display_hp()
    display_surface.blit(player.surface, player.rect)
    display_surface.blit(*display_score())
    pygame.display.update()