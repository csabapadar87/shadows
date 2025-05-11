import pygame
from pygame import Surface

class Planet:
    REGISTRY = []
 
    def __init__(
            self, 
            surface: Surface, 
            # x: int = 0, 
            # y: int = 0, 
            color: tuple[int, int, int] = (255, 0, 0), 
            rad: float = 5.0,
            width: int = 0,
            ) -> None:      
        self.surface = surface
        self.color = color
        self.radius = rad
        self.width = width # TODO: change hardcoded value later
        Planet.REGISTRY.append(self)

    def set_pos(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)

    def draw(self) -> None:
        if hasattr(self, 'pos'):
            pygame.draw.circle(
                surface=self.surface, 
                color=self.color, 
                radius=self.radius, 
                center=self.pos, 
                width=self.width
                )
        else:
            raise AttributeError("Cannot draw a planet object if it doesn't have a position!")