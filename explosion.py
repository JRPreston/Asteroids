from typing import override
import random
import pygame
import circleshape
from constants import EXPLOSION_SPEED

class ExplosionParticle(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, 1)
        self.exist_timer = 0

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        self.exist_timer += dt
        if self.exist_timer > 0.25:
            self.kill()
