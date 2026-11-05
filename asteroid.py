import logger
import random
import pygame
import circleshape
from explosion import ExplosionParticle
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH, EXPLOSION_SPEED

class Asteroid(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            logger.log_event("asteroid_split")
            angle = random.uniform(20, 50)
            baby1rot = self.velocity.rotate(angle)
            baby2rot = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            baby1 = Asteroid(self.position[0], self.position[1], new_radius)
            baby2 = Asteroid(self.position[0], self.position[1], new_radius)
            baby1.velocity = baby1rot * 1.2
            baby2.velocity = baby2rot * 1.2

    def explode(self):
        for i in range(10):
            particle = ExplosionParticle(self.position[0], self.position[1], self.radius)
            unit_vector = pygame.Vector2(0, 1)
            rotated_vector = unit_vector.rotate(random.randint(0, 360))
            rotated_with_speed_vector = rotated_vector * EXPLOSION_SPEED
            particle.velocity += rotated_with_speed_vector
