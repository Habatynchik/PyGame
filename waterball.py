import pygame

class WaterBall:
    def __init__(self, position):
        self.size = 50
        self.speed = 500
        self.surface = pygame.image.load('./images/WaterBall.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.size, self.size))
        self.rect = self.surface.get_rect()
        self.rect.center = position
        self.define_direction()

    def define_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        wb_pos = pygame.Vector2(self.rect.center)
        dir_x = mouse_pos.x - wb_pos.x
        dir_y = mouse_pos.y - wb_pos.y
        if dir_x == 0: dir_x = 0.0001
        if dir_y == 0: dir_y = 0.0001
        return pygame.Vector2(dir_x, dir_y).normalize()

    def update(self, delta_time):
        self.rect.center += self.define_direction() * delta_time * self.speed

    def shoot(self):
        pass