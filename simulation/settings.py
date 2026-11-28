
"""Central configuration for the EvoWorld simulation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Store the initial configuration of EvoWorld."""

    # Display settings
    window_width: int = 1200
    window_height: int = 800
    window_title: str = "EvoWorld — Artificial Evolution Simulation"
    background_color: tuple[int, int, int] = (15, 24, 32)  # Dark blue-grey background color
    target_fps: int = 60

    # Simulation timing
    updates_per_second: int = 30

    # World settings
    world_width: int = 1200
    world_height: int = 800

    # Initial ecosystem settings
    initial_population: int = 100
    initial_food_count: int = 200

    # Organism settings
    organism_radius: int = 6
    organism_color: tuple[int, int, int] = (96, 165, 250)

    # Food settings
    food_energy: float = 25.0
    food_radius: int = 3
    food_color: tuple[int, int, int] = (80, 200, 120)

    # Reproducibility
    random_seed: int = 42


# Shared default configuration
DEFAULT_SETTINGS = Settings()
