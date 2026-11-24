
"""Central configuration for the EvoWorld simulation."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Settings:
    """Store the initial configuration of EvoWorld."""

    # Display settings
    window_width: int = 1200
    window_height: int = 800
    target_fps: int = 60

    # World settings
    world_width: int = 1200
    world_height: int = 800

    # Initial ecosystem settings
    initial_population: int = 100
    initial_food_count: int = 200

    # Reproducibility
    random_seed: int = 42


# Shared default configuration
DEFAULT_SETTINGS = Settings()
