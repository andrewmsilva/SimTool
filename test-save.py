from src.SimTool import Model

model = Model()

model.createGenerator(
    name='Begin',
    target='Reception',
    min_range=3,
    max_range=8,
    distribution='normal',
    max_entities=10,
    entity_name='Patient'
)

model.createProcess(
    name='Reception',
    target='Medical',
    min_range=8,
    max_range=15,
    distribution='normal',
    num_resources=2,
    resource_name='Receptionist'
)

model.createProcess(
    name='Medical',
    target='Pharmacy',
    min_range=15,
    max_range=25,
    distribution='normal',
    num_resources=3,
    resource_name='Doctor'
)

model.createProcess(
    name='Pharmacy',
    target='End',
    min_range=5,
    max_range=8,
    distribution='normal',
    num_resources=None,
    resource_name='Pharmaceutical'
)

model.createTerminator(name='End')

model.save('model.csv')
model.run()