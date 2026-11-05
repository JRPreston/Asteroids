from typing import override
import pygame
import circleshape
from constants import SHOT_RADIUS

class Shot(circleshape.CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, SHOT_RADIUS)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
