
"""Coordinate the EvoWorld ecosystem independently of rendering."""

import random

from environment.environment import Environment
from organisms.population import Population
from simulation.settings import DEFAULT_SETTINGS, Settings
from simulation.world import World


class Simulation:
    """Own ecosystem state and advance it in fixed steps."""

    def __init__(self, settings: Settings = DEFAULT_SETTINGS) -> None:
        rate = settings.updates_per_second
        if type(rate) is not int or rate <= 0:
            raise ValueError("Updates per second must be a positive integer.")

        self.settings = settings
        self.rng = random.Random(settings.random_seed)
        self.world = World(settings.world_width, settings.world_height, self.rng)
        self.environment = Environment(self.world, settings)
        self.population = Population(self.world, settings)
        self.step_count = 0
        self._pending_units = 0

    @property
    def timestep(self) -> float:
        """Return the duration of one simulation step in seconds."""
        return 1 / self.settings.updates_per_second

    @property
    def elapsed_time(self) -> float:
        """Return simulated time in seconds."""
        return self.step_count * self.timestep

    def update(self) -> None:
        """Advance one step; biological mechanics arrive in Phase 2."""
        self.step_count += 1

    def advance(self, elapsed_ms: int) -> int:
        """Run all fixed steps due for the supplied elapsed milliseconds."""
        if type(elapsed_ms) is not int or elapsed_ms < 0:
            raise ValueError("Elapsed milliseconds must be a nonnegative integer.")

        self._pending_units += elapsed_ms * self.settings.updates_per_second
        steps, self._pending_units = divmod(self._pending_units, 1000)

        for _ in range(steps):
            self.update()

        return steps
