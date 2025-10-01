import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        center = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", center, self.radius, width=2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(float(20), float(50))
        vect1 = self.velocity.rotate(angle)
        vect2 = self.velocity.rotate(-angle)
        smol_radius = self.radius - ASTEROID_MIN_RADIUS
        smol_asteroid1 = Asteroid(self.position.x, self.position.y, smol_radius)
        smol_asteroid2 = Asteroid(self.position.x, self.position.y, smol_radius)
        smol_asteroid1.velocity = vect1 * 1.2
        smol_asteroid2.velocity = vect2 * 1.2
