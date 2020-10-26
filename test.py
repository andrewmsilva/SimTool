from src.SimTool import Enviroment

env = Enviroment()
env.createGenerator('Test', 'test', (0, 8), 'normal')
env.run(5)