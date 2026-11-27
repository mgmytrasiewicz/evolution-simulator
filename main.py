
"""EvoWorld application entry point."""

import random

import pygame

from environment.environment import Environment
from organisms.population import Population
from simulation.world import World
from simulation.settings import DEFAULT_SETTINGS
from visualization.renderer import Renderer


def main() -> None:
    """Start the EvoWorld application."""

    pygame.init()

    try:

        rng = random.Random(DEFAULT_SETTINGS.random_seed)

        world = World(
            DEFAULT_SETTINGS.world_width,
            DEFAULT_SETTINGS.world_height,
            rng,
        )

        environment = Environment(world, DEFAULT_SETTINGS)
        population = Population(world, DEFAULT_SETTINGS)

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
            renderer.render(
                environment.food,
                population.organisms
            )

            #Limint the frame rate to the target FPS
            clock.tick(DEFAULT_SETTINGS.target_fps)

    finally:
        #Quit Pygame and clean up resources
        pygame.quit()

if __name__ == "__main__":
    main()
