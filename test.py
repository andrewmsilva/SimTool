from src.SimTool import Enviroment

env = Enviroment()

env.createGenerator(
    name='chegada',
    target='recepção',
    min_range=2,
    max_range=5,
    distribution='normal',
    entity_name='paciente'
)

env.createProcess(
    name='recepção',
    target='consulta',
    min_range=7,
    max_range=12,
    distribution='normal',
    num_resources=2,
    resource_name='atendente'
)

env.createProcess(
    name='consulta',
    target='saída',
    min_range=15,
    max_range=25,
    distribution='normal',
    resource_name='médico'
)

env.createTerminator(name='saída')

env.run(stop_at=30)