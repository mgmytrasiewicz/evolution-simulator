
import random

import pytest

from simulation.world import World


@pytest.fixture
def world():
    """Create a standard test world."""

    rng = random.Random(42)
    return World(1200, 800, rng)


def test_world_initialization(world):
    assert world.width == 1200
    assert world.height == 800


def test_world_rejects_invalid_dimensions():
    rng = random.Random(42)

    with pytest.raises(ValueError):
        World(0, 800, rng)

    with pytest.raises(ValueError):
        World(1200, -100, rng)

    with pytest.raises(ValueError):
        World(float("inf"), 800, rng)


def test_position_inside_world(world):
    assert world.is_position_inside((500, 300))


def test_position_outside_world(world):
    assert not world.is_position_inside((1300, 300))
    assert not world.is_position_inside((500, 900))
    assert not world.is_position_inside((-10, 300))


def test_boundary_position_is_outside(world):
    assert not world.is_position_inside((1200, 400))
    assert not world.is_position_inside((400, 800))


def test_clamp_position(world):
    position = world.clamp_position((1300, 900))

    assert world.is_position_inside(position)


def test_clamp_negative_position(world):
    position = world.clamp_position((-100, -50))

    assert position == (0.0, 0.0)


def test_clamp_position_rejects_non_finite_values(world):
    with pytest.raises(ValueError):
        world.clamp_position((float("nan"), 100))


def test_random_position_is_inside_world(world):
    for _ in range(1000):
        position = world.random_position()
        assert world.is_position_inside(position)


def test_random_positions_are_reproducible():
    world_1 = World(1200, 800, random.Random(42))
    world_2 = World(1200, 800, random.Random(42))

    positions_1 = [
        world_1.random_position()
        for _ in range(100)
    ]

    positions_2 = [
        world_2.random_position()
        for _ in range(100)
    ]

    assert positions_1 == positions_2
