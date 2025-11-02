import random

import pygame

class Player:
    def __init__(self, speed, display_surface):
        self.prev_direction = None
        self.hp = 100
        self.size = (100, 100)
        self.speed = speed
        self.display_surface = display_surface

        self.walk_animation_frame = 0
        self.walk_animation = []
        for i in range(4):
            frame = pygame.image.load(f"./images/Player/Player_Run_{i + 1}.png").convert_alpha()
            frame = pygame.transform.scale(frame, self.size)
            self.walk_animation.append(frame)
            
        self.idle_animation = pygame.image.load('./images/Player/Player_1.png').convert_alpha()
        self.idle_animation = pygame.transform.scale(self.idle_animation, self.size)
        self.idle_animation_left = pygame.transform.flip(self.idle_animation, True, False)

        self.surface = self.idle_animation
        self.rect = self.surface.get_rect()
        self.rect.bottom = display_surface.get_rect().bottom
        self.is_flipped = False
        self.direction = pygame.Vector2(0, 0)
        #sound initialization
        self.footstep_sound = pygame.mixer.Sound('./sounds/Steps.ogg')
        self.footstep_time = 0

    def play_footstep_sound(self):
        if self.direction and self.footstep_time + 200 < pygame.time.get_ticks():
            self.footstep_sound.play()
            self.footstep_time = pygame.time.get_ticks()

    def move(self, key, delta_time):
        #When we move out of bounds, we return to the other side.
        if self.rect.bottom < 0:
            self.rect.top = self.display_surface.get_rect().bottom
        if self.rect.top > self.display_surface.get_rect().bottom:
            self.rect.bottom = 0
        if self.rect.right < 0:
            self.rect.left = self.display_surface.get_rect().right
        if self.rect.left > self.display_surface.get_rect().right:
            self.rect.right = 0

        #Set the direction vector.
        self.direction.x = int(key[pygame.K_d]) - int(key[pygame.K_a])
        self.direction.y = int(key[pygame.K_s]) - int(key[pygame.K_w or pygame.K_UP])

        if self.direction:
            self.direction = self.direction.normalize()
        self.rect.center += self.direction * delta_time * self.speed
        self.play_footstep_sound()
        #Change the animation.
        if self.direction:
            self.surface = self.walk_animation[int(self.walk_animation_frame / 3) % 4]
            self.walk_animation_frame += 1
        else:
            self.walk_animation_frame = 0

        #Set the direction of the player.
        if self.direction.x != 0 or self.direction.y != 0:
            self.prev_direction = self.direction.x
        if self.direction.x == 0 and self.direction.y == 0:
            if self.prev_direction == -1:
                self.surface = self.idle_animation_left
            elif self.prev_direction == 1:
                self.surface = self.idle_animation

        if self.direction.x == -1:
            self.is_flipped = True
            self.surface = pygame.transform.flip(self.surface, True, False)
        if self.direction.x == 1 and self.is_flipped == True:
            self.is_flipped = False
            self.surface = pygame.transform.flip(self.surface, True, False)
