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

## Example


The file [test.py](https://github.com/andrewmsilva/SimTool/blob/main/test.py) presents an example of a model simulating the behavior of a fictional medical clinic. The resulting log is in the following.

```
Reception: Patient 0 entered the queue at 4
Reception: Patient 0 started the process at 4 by Receptionist 0
Reception: Patient 1 entered the queue at 8
Reception: Patient 1 started the process at 8 by Receptionist 1
Reception: Patient 2 entered the queue at 12
Reception: Patient 0 finished the process at 14 with duration 10
Medical: Patient 0 entered the queue at 14
Reception: Patient 2 started the process at 14 by Receptionist 0
Medical: Patient 0 started the process at 14 by Doctor 0
Reception: Patient 3 entered the queue at 16
Reception: Patient 1 finished the process at 17 with duration 9
Medical: Patient 1 entered the queue at 17
Reception: Patient 3 started the process at 17 by Receptionist 1
Reception: Patient 4 entered the queue at 21
Reception: Patient 2 finished the process at 22 with duration 8
Medical: Patient 2 entered the queue at 22
Reception: Patient 4 started the process at 22 by Receptionist 0
Reception: Patient 5 entered the queue at 26
Reception: Patient 3 finished the process at 27 with duration 10
Medical: Patient 3 entered the queue at 27
Reception: Patient 5 started the process at 27 by Receptionist 1
Reception: Patient 4 finished the process at 31 with duration 9
Medical: Patient 4 entered the queue at 31
Reception: Patient 5 finished the process at 35 with duration 8
Medical: Patient 5 entered the queue at 35
Medical: Patient 0 finished the process at 39 with duration 25
End: Patient 0 finished the simulation at 39
Medical: Patient 1 started the process at 39 by Doctor 0
Medical: Patient 1 finished the process at 55 with duration 16
End: Patient 1 finished the simulation at 55
Medical: Patient 2 started the process at 55 by Doctor 0
Medical: Patient 2 finished the process at 78 with duration 23
End: Patient 2 finished the simulation at 78
Medical: Patient 3 started the process at 78 by Doctor 0
Medical: Patient 3 finished the process at 99 with duration 21
End: Patient 3 finished the simulation at 99
Medical: Patient 4 started the process at 99 by Doctor 0
Medical: Patient 4 finished the process at 119 with duration 20
End: Patient 4 finished the simulation at 119
Medical: Patient 5 started the process at 119 by Doctor 0
Medical: Patient 5 finished the process at 139 with duration 20
End: Patient 5 finished the simulation at 139
Simulation ended
```
