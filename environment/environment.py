"""Manage environmental resources."""

import math

from environment.food import Food
from simulation.settings import Settings
from simulation.world import World


class Environment:
    """Own the food collection and generate its initial contents."""

    def __init__(self, world: World, settings: Settings) -> None:
        if settings.initial_food_count < 0:
            raise ValueError("Initial food count cannot be negative.")

        if not math.isfinite(settings.food_energy) or settings.food_energy <= 0:
            raise ValueError("Food energy must be positive and finite.")

        self.world = world
        self.food: list[Food] = []

        for food_id in range(settings.initial_food_count):
            self.food.append(
                Food(
                    food_id,
                    world.random_position(),
                    settings.food_energy,
                )
            )