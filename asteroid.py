import pygame

from circleshape import CircleShape

CIRCLE_WIDTH = 2

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, CIRCLE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
