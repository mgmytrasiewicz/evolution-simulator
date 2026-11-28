
"""EvoWorld application entry point."""

import random

import pygame

from simulation.simulation import Simulation
from simulation.settings import DEFAULT_SETTINGS
from visualization.renderer import Renderer


def main() -> None:
    """Start the EvoWorld application."""

    pygame.init()

    try:

        simulation = Simulation(DEFAULT_SETTINGS)
        renderer = Renderer(DEFAULT_SETTINGS)
        clock = pygame.time.Clock()
        running = True

        #Main application loop
        while running:

            #Calculate elapsed time since last frame
            elapsed_ms = clock.tick(DEFAULT_SETTINGS.target_fps)

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

            #Advance the simulation by the elapsed time
            simulation.advance(elapsed_ms)

            #Render the current frame
            renderer.render(
                simulation.environment.food,
                simulation.population.organisms
            )

            #Limint the frame rate to the target FPS
            clock.tick(DEFAULT_SETTINGS.target_fps)

    finally:
        #Quit Pygame and clean up resources
        pygame.quit()

if __name__ == "__main__":
    main()
