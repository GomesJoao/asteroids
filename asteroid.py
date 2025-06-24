from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,color="white",center=self.position, radius=self.radius, width=2)

    def update(self, dt):
        # moves in a straight line at constant speed
        self.position += (self.velocity*dt) 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            v1 = pygame.math.Vector2.rotate(self.velocity, angle)
            v2 = pygame.math.Vector2.rotate(self.velocity, -angle)
            newRadius = self.radius - ASTEROID_MIN_RADIUS
            a1 = Asteroid(self.position.x, self.position.y, newRadius)
            a2 = Asteroid(self.position.x, self.position.y, newRadius)
            a1.velocity = v1*1.2
            a2.velocity = v2*1.2