from src.SimTool import Enviroment

env = Enviroment()
env.createService('Recepção', (4, 8), num_servers=2, distribution='normal')
env.createGenerator('Pacientes', 'Recepção', (0, 8), max_generation=60, distribution='normal')
env.run()