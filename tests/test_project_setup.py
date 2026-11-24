
"""Tests for the initial EvoWorld project setup."""

from simulation.settings import DEFAULT_SETTINGS, Settings


def test_default_settings_exist():
    """Verify that the default configuration is available."""

    assert isinstance(DEFAULT_SETTINGS, Settings)


def test_world_dimensions_are_valid():
    """Verify that world dimensions are positive."""

    assert DEFAULT_SETTINGS.world_width > 0
    assert DEFAULT_SETTINGS.world_height > 0


def test_initial_population_is_valid():
    """Verify that the initial population is positive."""

    assert DEFAULT_SETTINGS.initial_population > 0


def test_initial_food_count_is_valid():
    """Verify that the initial food count is positive."""

    assert DEFAULT_SETTINGS.initial_food_count > 0


def test_random_seed_is_configured():
    """Verify that a random seed is configured."""

    assert isinstance(DEFAULT_SETTINGS.random_seed, int)
