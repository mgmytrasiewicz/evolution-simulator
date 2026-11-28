"""Integration tests for the headless simulation controller."""

from dataclasses import replace

import pytest

from simulation.settings import DEFAULT_SETTINGS
from simulation.simulation import Simulation


def test_initial_ecosystem():
    sim = Simulation()
    assert sim.world.width == DEFAULT_SETTINGS.world_width
    assert sim.world.height == DEFAULT_SETTINGS.world_height
    assert len(sim.environment.food) == DEFAULT_SETTINGS.initial_food_count
    assert len(sim.population.organisms) == DEFAULT_SETTINGS.initial_population
    assert sim.environment.world is sim.population.world is sim.world
    assert sim.world.rng is sim.rng
    assert all(sim.world.is_position_inside(item.position)
               for item in sim.environment.food + sim.population.organisms)
    assert len({o.organism_id for o in sim.population.organisms}) == len(
        sim.population.organisms
    )


def test_initial_clock():
    sim = Simulation()
    assert sim.step_count == 0
    assert sim.elapsed_time == 0
    assert sim.timestep == pytest.approx(1 / 30)


def test_single_update():
    sim = Simulation()
    sim.update()
    assert sim.step_count == 1
    assert sim.elapsed_time == pytest.approx(sim.timestep)


def test_headless_steps():
    sim = Simulation()
    for _ in range(1000):
        sim.update()
    assert sim.step_count == 1000


def test_seed_reproducibility():
    first, second = Simulation(), Simulation()
    assert first.environment.food == second.environment.food
    assert first.population.organisms == second.population.organisms


def test_update_preserves_initial_entities():
    sim = Simulation()
    before = Simulation()
    sim.advance(1000)
    assert sim.environment.food == before.environment.food
    assert sim.population.organisms == before.population.organisms


@pytest.mark.parametrize("frames", [10, 30, 60, 120])
def test_frame_partition_independence(frames):
    sim = Simulation()
    for i in range(frames):
        sim.advance((i + 1) * 1000 // frames - i * 1000 // frames)
    assert sim.step_count == 30
    assert sim.elapsed_time == pytest.approx(1)


def test_fractional_step_is_retained():
    sim = Simulation()
    assert sim.advance(33) == 0
    assert sim.advance(1) == 1
    assert sim.advance(66) == 2
    assert sim.step_count == 3


def test_custom_update_rate():
    sim = Simulation(replace(DEFAULT_SETTINGS, updates_per_second=20))
    assert sim.advance(1000) == 20
    assert sim.timestep == pytest.approx(0.05)


@pytest.mark.parametrize("rate", [0, -1, 2.5, True])
def test_invalid_update_rate(rate):
    with pytest.raises(ValueError):
        Simulation(replace(DEFAULT_SETTINGS, updates_per_second=rate))


@pytest.mark.parametrize("elapsed", [-1, 1.5, True])
def test_invalid_elapsed_time(elapsed):
    sim = Simulation()
    with pytest.raises(ValueError):
        sim.advance(elapsed)
    assert sim.step_count == 0
