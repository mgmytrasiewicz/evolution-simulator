
"""Manage the initial organism population."""

from organisms.organism import Organism
from simulation.settings import Settings
from simulation.world import World


class Population:
    """Own the collection of organisms."""

    def __init__(self, world: World, settings: Settings) -> None:
        if settings.initial_population < 0:
            raise ValueError("Initial population cannot be negative.")

        radius = settings.organism_radius

        if not isinstance(radius, int) or radius <= 0:
            raise ValueError(
                "Organism radius must be a positive integer."
            )

        self.world = world
        self.organisms: list[Organism] = []

        for organism_id in range(settings.initial_population):
            self.organisms.append(
                Organism(
                    organism_id,
                    world.random_position(),
                    radius,
                )
            )
