# EvoWorld

A modular 2D artificial-life and evolution simulator built with Python.

## Project overview

EvoWorld aims to demonstrate evolution emerging from inherited variation, mutation, resource competition and differential reproduction. The planned initial reproduction model is asexual. Phase 1 establishes the technical foundation; organisms do not yet move, eat, age or reproduce.

## Development status

**Phase 1 — Foundation:** all seven tasks implemented; 59 automated tests passed on the reviewed snapshot (Python 3.13.5). Windows graphical verification and local milestone approval remain pending. Proposed milestone: `v0.1.0`.

See [Phase 1 completion report](docs/phase1-completion-report.md) for evidence, limitations and release checks. Next planned task: Phase 2, Task 1 — Random Organism Movement.

## Getting started (Windows / VS Code)

Open the project folder in VS Code and run these commands in PowerShell. For an existing virtual environment, skip its creation.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest -q
python main.py
```

The requirements file is preserved from the development snapshot; a fresh dependency installation has not been verified in the report environment. Use your existing working environment if available.

The window should show blue organisms and green food on a dark background. Close with Escape or the window close button. Stationary entities are expected in Phase 1.

## Configuration

Defaults are defined in `simulation/settings.py`:

| Setting | Default |
| --- | --- |
| World and window dimensions | 1200 × 800 |
| Initial organisms | 100 |
| Initial food items | 200 |
| Rendering FPS limit | 60 |
| Simulation updates per second | 30 |
| Random seed | 42 |
| Organism radius | 6 |
| Food radius | 3 |
| Food energy value | 25.0 |

Food energy is stored but not consumed yet.

## Architecture

```text
main.py                     # Application loop and event handling
simulation/
  settings.py               # Immutable configuration
  simulation.py             # Controller, clock and fixed-step scheduling
  world.py                  # Coordinates, boundaries and random positions
organisms/
  organism.py               # Individual organism data
  population.py             # Initial population and IDs
  genome.py, genetics.py, behavior.py  # Future mechanics
environment/               # Food data and environment initialization
visualization/             # Pygame renderer; future dashboard
analytics/                 # Future statistics
tests/                     # Automated tests
docs/                      # Milestone documentation
```

`Simulation` owns a shared world, environment and population. The world uses the simulation's seeded random generator. `main.py` supplies elapsed milliseconds to `Simulation.advance()` and passes entity collections to the renderer. The simulation core does not import Pygame. Rendering and simulation updates have separate rates.

## Headless use and tests

```python
from simulation.simulation import Simulation

sim = Simulation()
for _ in range(1000):
    sim.update()
print(sim.step_count)  # 1000
```

Run `python -m pytest -q` from the project root. Expected baseline: 59 passing tests. Tests cover initialization, boundaries, unique IDs, seeded reproducibility and fixed-step scheduling. There is no command-line headless mode yet.

## Technology and roadmap

Python, Pygame, pytest and Git are the foundation. NumPy and Matplotlib are planned for numerical work and analytics; JSON is planned for persistence.

1. Foundation — implemented; local verification pending.
2. Survival — movement, food detection, consumption, energy, aging and death.
3. Genetics and reproduction — inheritance and mutation.
4. Natural selection — competition and adaptation.
5. Complex ecosystem — predation and diversification.
6. Advanced behavior — evolved strategies and neural networks.
7. Complete application — persistence, analytics, optimization and testing.

Do not interpret Phase 1 as a completed evolutionary MVP.
