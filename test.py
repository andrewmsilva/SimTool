from src.SimTool import Enviroment

env = Enviroment()
env.createGenerator('Paciente', 'Recepção', 1, 8, 'normal')
env.createService('Recepção', 'Médicos', 3, 7, 'normal', 2)
env.createService('Médicos', 'Fim', 8, 14, 'normal', 3)
env.createTerminator('Fim')
env.run(stop_at=40)