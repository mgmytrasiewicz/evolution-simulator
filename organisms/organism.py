
"""Represent individual organisms in the simulation."""

from dataclasses import dataclass


@dataclass
class Organism:
    """Represent an individual organism in the virtual world."""

    organism_id: int
    position: tuple[float, float]
    radius: float
