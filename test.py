from src.SimTool import Enviroment

env = Enviroment()
env.createService('Recepção', 'Médicos', 3, 7, 'normal', 2)
env.createGenerator('Paciente', 'Recepção', 1, 8, 'normal')
env.run(stop_at=60)