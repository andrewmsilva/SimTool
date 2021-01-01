from src.SimTool import Model

try:
    model = Model.load('model.csv')
except:
    model = Model()

    model.createGenerator(
        name='Begin',
        target='Reception',
        min_range=2,
        max_range=5,
        distribution='normal',
        max_entities=10,
        entity_name='Patient'
    )

    model.createProcess(
        name='Reception',
        target='Medical',
        min_range=7,
        max_range=12,
        distribution='normal',
        num_resources=2,
        resource_name='Receptionist'
    )

    model.createProcess(
        name='Medical',
        target='End',
        min_range=15,
        max_range=25,
        distribution='normal',
        resource_name='Doctor'
    )

    model.createTerminator(name='End')

    model.save('model.csv')

model.run()