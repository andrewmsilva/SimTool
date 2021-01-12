from src.SimTool import Model

model = Model()

model.createGenerator(
    name='Entry',
    target='Reception',
    min_range=3,
    max_range=8,
    distribution='normal',
    max_entities=1000,
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
    target='Assistent',
    min_range=15,
    max_range=25,
    distribution='normal',
    num_resources=3,
    resource_name='Doctor'
)

model.createRouter(
    name='Assistent',
    targets=['Pharmacy', 'Exit'],
    distribution='uniform'
)

model.createProcess(
    name='Pharmacy',
    target='Exit',
    min_range=5,
    max_range=8,
    distribution='normal',
    num_resources=None,
    resource_name='Pharmaceutical'
)

model.createTerminator(name='Exit')

model.save('model.csv')
model.run(random_state=0)