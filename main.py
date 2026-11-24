
"""EvoWorld application entry point."""

from simulation.settings import DEFAULT_SETTINGS


def main() -> None:
    """Start the EvoWorld application."""

    print("================================")
    print("          EvoWorld")
    print("  Artificial Evolution Simulator")
    print("================================")

    print(f"World size: {DEFAULT_SETTINGS.world_width} x "
          f"{DEFAULT_SETTINGS.world_height}")

    print(f"Initial population: "
          f"{DEFAULT_SETTINGS.initial_population}")

    print(f"Initial food: {DEFAULT_SETTINGS.initial_food_count}")

    print(f"Random seed: {DEFAULT_SETTINGS.random_seed}")

    print("\nProject initialized successfully!")


if __name__ == "__main__":
    main()
