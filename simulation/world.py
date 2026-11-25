
"""Represent the two-dimensional EvoWorld environment."""

import math
import random


class World:
    """Represent the dimensions and boundaries of the simulation world."""

    def __init__(
        self,
        width: float,
        height: float,
        rng: random.Random,
    ) -> None:
        """Initialize the world with dimensions and a random generator."""

        if not math.isfinite(width) or width <= 0:
            raise ValueError("World width must be a positive finite number.")

        if not math.isfinite(height) or height <= 0:
            raise ValueError("World height must be a positive finite number.")

        self.width = float(width)
        self.height = float(height)
        self.rng = rng

    def is_position_inside(self, position: tuple[float, float]) -> bool:
        """Check whether a position is inside the world."""

        x, y = position

        return (
            math.isfinite(x)
            and math.isfinite(y)
            and 0 <= x < self.width
            and 0 <= y < self.height
        )

    def clamp_position(
        self, position: tuple[float, float]
    ) -> tuple[float, float]:
        """Correct a position so it remains inside the world."""

        x, y = position

        if not math.isfinite(x) or not math.isfinite(y):
            raise ValueError("Position coordinates must be finite numbers.")

        max_x = math.nextafter(self.width, 0.0)
        max_y = math.nextafter(self.height, 0.0)

        return (
            max(0.0, min(x, max_x)),
            max(0.0, min(y, max_y)),
        )

    def random_position(self) -> tuple[float, float]:
        """Generate a random position inside the world."""

        x = self.rng.random() * self.width
        y = self.rng.random() * self.height

        return x, y
