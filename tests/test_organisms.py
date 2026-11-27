
"""Tests for the Organism data model."""

from organisms.organism import Organism


def test_organism_creation():
    organism = Organism(
        organism_id=1,
        position=(100.0, 200.0),
        radius=6.0,
    )

    assert organism.organism_id == 1
    assert organism.position == (100.0, 200.0)
    assert organism.radius == 6.0


def test_organism_position_can_change():
    organism = Organism(
        organism_id=1,
        position=(100.0, 200.0),
        radius=6.0,
    )

    organism.position = (150.0, 250.0)

    assert organism.position == (150.0, 250.0)


def test_organisms_have_independent_state():
    first = Organism(1, (100.0, 200.0), 6.0)
    second = Organism(2, (300.0, 400.0), 6.0)

    first.position = (150.0, 250.0)

    assert first.position == (150.0, 250.0)
    assert second.position == (300.0, 400.0)
    assert first.organism_id != second.organism_id
