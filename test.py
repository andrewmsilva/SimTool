from src.SimTool import Model

model = Model()

model.createGenerator(
    name='chegada',
    target='recepção',
    min_range=2,
    max_range=5,
    distribution='normal',
    entity_name='paciente'
)

model.createProcess(
    name='recepção',
    target='roteador',
    min_range=7,
    max_range=12,
    distribution='normal',
    num_resources=2,
    resource_name='atendente'
)

model.createRouter(
    name='roteador',
    targets=['consulta', 'saída'],
    distribution='uniform'
)

model.createProcess(
    name='consulta',
    target='recepção',
    min_range=15,
    max_range=25,
    distribution='normal',
    resource_name='médico'
)

model.createTerminator(name='saída')

model.run(stop_at=30)