# SimTool

SimTool is an experimental framework for creating general simulation models.

```python
from src.SimTool import Model

model = Model()
```

## Components

### Generator

Generators create entities according to a time interval with a random distribution (uniform or normal).

```python
model.createGenerator(
    name='Begin',
    target='Reception',
    min_range=2,
    max_range=5,
    distribution='normal',
    entity_name='Patient'
)
```

### Process

Processes subject generated entities to a process executed by some resources with duration in a time interval with a random distribution (uniform or normal).

```python
model.createProcess(
    name='Reception',
    target='Router',
    min_range=7,
    max_range=12,
    distribution='normal',
    num_resources=2,
    resource_name='Receptionist'
)
```

### Router

Routers send entities to other target components with a random distribution (uniform or normal).

```python
model.createRouter(
    name='Router',
    targets=['Medical', 'End'],
    distribution='uniform'
)
```

### Terminator

Terminators receive entities that finished the simulation.

```python
model.createTerminator(name='End')
```

## Simulating

After creating all components in a model, just call the `run` method.

```python
model.run(stop_at=30)
```
