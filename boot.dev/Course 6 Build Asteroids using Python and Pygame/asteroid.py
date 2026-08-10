from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if ASTEROID_MIN_RADIUS < self.radius:
            log_event("asteroid_split")
            new_asteroid_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            new_asteroid_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            split_angle = random.uniform(20,50)
            new_asteroid_1.velocity = 1.2 * self.velocity.rotate(split_angle)
            new_asteroid_2.velocity = 1.2 * self.velocity.rotate(-split_angle)