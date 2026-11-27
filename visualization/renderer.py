
"""Pygame rendering system for EvoWorld."""

import pygame

from environment.food import Food
from organisms.organism import Organism
from simulation.settings import Settings


class Renderer:
    """Handle graphical presentation of the EvoWorld application."""

    def __init__(self, settings: Settings) -> None:
        """Initialize the application window."""

        self.settings = settings

        self.screen = pygame.display.set_mode(
            (
                settings.window_width,
                settings.window_height,
            )
        )

        pygame.display.set_caption(settings.window_title)

    def render(
            self, 
            food: list[Food],
            organisms: list[Organism]
        ) -> None:
        """Draw and display one frame."""

        self.screen.fill(self.settings.background_color)

        for item in food:
            x, y = item.position

            pygame.draw.circle(
                self.screen,
                self.settings.food_color,
                (int(x), int(y)),
                self.settings.food_radius,
            )

        for organism in organisms:
            x, y = organism.position

            pygame.draw.circle(
                self.screen,
                self.settings.organism_color,
                (int(x), int(y)),
                self.settings.organism_radius,
            )

        pygame.display.flip()
