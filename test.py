from src.SimTool import Enviroment

env = Enviroment()
env.createService('Recepção', "None", (4, 8), num_servers=2, distribution='normal')
env.createGenerator('Pacientes', 'Recepção', (1, 8), distribution='normal')
env.run(stop_at=60)