
"""Verify population generation without Pygame."""

import random
from dataclasses import replace

import pytest

from organisms.population import Population
from simulation.settings import DEFAULT_SETTINGS
from simulation.world import World


def make_population(**changes):
    settings = replace(DEFAULT_SETTINGS, **changes)

    world = World(
        settings.world_width,
        settings.world_height,
        random.Random(settings.random_seed),
    )

    return Population(world, settings)


def test_population_count():
    population = make_population(initial_population=10)

    assert len(population.organisms) == 10


def test_unique_ids():
    organisms = make_population().organisms

    assert len({
        organism.organism_id
        for organism in organisms
    }) == len(organisms)


def test_positions():
    population = make_population()

    assert all(
        population.world.is_position_inside(organism.position)
        for organism in population.organisms
    )


def test_radius():
    population = make_population(organism_radius=8)

    assert all(
        organism.radius == 8
        for organism in population.organisms
    )


def test_reproducibility():
    assert make_population().organisms == make_population().organisms


def test_empty_population():
    assert make_population(initial_population=0).organisms == []


def test_negative_population():
    with pytest.raises(ValueError):
        make_population(initial_population=-1)


@pytest.mark.parametrize(
    "radius",
    [0, -1, float("inf"), float("nan")],
)
def test_invalid_radius(radius):
    with pytest.raises(ValueError):
        make_population(organism_radius=radius)
