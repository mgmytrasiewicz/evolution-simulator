
"""EvoWorld application entry point."""

import pygame

from simulation.settings import DEFAULT_SETTINGS
from visualization.renderer import Renderer


def main() -> None:
    """Start the EvoWorld application."""

    pygame.init()

    try:

        renderer = Renderer(DEFAULT_SETTINGS)
        clock = pygame.time.Clock()

        running = True

        #Main application loop
        while running:

            #Handle application events
            for event in pygame.event.get():

                #Handle window close button
                if event.type == pygame.QUIT:
                    running = False

                #Handle keyboard input
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            if not running:
                break

            #Render the current frame
            renderer.render()

            #Limint the frame rate to the target FPS
            clock.tick(DEFAULT_SETTINGS.target_fps)

    finally:
        #Quit Pygame and clean up resources
        pygame.quit()

if __name__ == "__main__":
    main()
