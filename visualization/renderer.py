
"""Pygame rendering system for EvoWorld."""

import pygame

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

    def render(self) -> None:
        """Draw and display one frame."""

        self.screen.fill(self.settings.background_color)

        pygame.display.flip()
