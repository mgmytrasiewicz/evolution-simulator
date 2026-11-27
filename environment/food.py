"""Represent individual food resources."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Food:
    """A stationary resource with a position and stored energy."""

    food_id: int
    position: tuple[float, float]
    energy: float