"""Verify food generation without Pygame."""

import random
from dataclasses import replace

import pytest

from environment.environment import Environment
from simulation.settings import DEFAULT_SETTINGS
from simulation.world import World


def make_environment(**changes):
    settings = replace(DEFAULT_SETTINGS, **changes)

    world = World(
        settings.world_width,
        settings.world_height,
        random.Random(settings.random_seed),
    )

    return Environment(world, settings)


def test_food_count():
    assert len(make_environment().food) == DEFAULT_SETTINGS.initial_food_count


def test_food_positions():
    environment = make_environment()

    assert all(
        environment.world.is_position_inside(item.position)
        for item in environment.food
    )


def test_food_energy():
    assert all(
        item.energy == 12.0
        for item in make_environment(food_energy=12.0).food
    )


def test_unique_ids():
    food = make_environment().food

    assert len({item.food_id for item in food}) == len(food)


def test_reproducibility():
    assert make_environment().food == make_environment().food


def test_empty_environment():
    assert make_environment(initial_food_count=0).food == []


def test_negative_count():
    with pytest.raises(ValueError):
        make_environment(initial_food_count=-1)


@pytest.mark.parametrize(
    "energy",
    [0, -1, float("inf"), float("nan")],
)
def test_invalid_energy(energy):
    with pytest.raises(ValueError):
        make_environment(food_energy=energy)