import pygame

class WaterBall:
    def __init__(self, position):
        self.size = 50
        self.speed = 500
        self.surface = pygame.image.load('./images/WaterBall.png').convert_alpha()
        self.surface = pygame.transform.scale(self.surface, (self.size, self.size))
        self.rect = self.surface.get_rect()
        self.rect.center = position

    def define_direction(self):
        mouse_pos = pygame.Vector2(pygame.mouse.get_pos())
        wb_pos = pygame.Vector2(self.rect.center)
        dir_x = mouse_pos.x - wb_pos.x
        dir_y = mouse_pos.y - wb_pos.y
        return pygame.Vector2(dir_x, dir_y).normalize()

        pass

